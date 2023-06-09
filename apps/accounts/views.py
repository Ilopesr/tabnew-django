from decouple import config

from django.views.generic import FormView, TemplateView, View
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

from apps.accounts.forms import (AccountForm,
                                 RecoverPasswordForm,
                                 ChangePasswordForm,
                                 NewAccountForm,
                                 LoginForm
                                 )
from apps.accounts.models import Account


class NewAccountView(FormView):
    template_name = "pages/accounts/signup.html"
    form_class = NewAccountForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        username_check = Account.objects.filter(username=username).exists()
        email_check = Account.objects.filter(email=email).exists()

        if username_check:
            messages.error(
                self.request, "Nome de usuário existente, tente outro.")
            return redirect('signup')
        else:
            if email_check:
                messages.error(self.request, "Email existente, tente outro.")
                return redirect('signup')
            else:
                try:
                    user = Account.objects.create_user(
                        username=username,
                        email=email,
                        is_active=False,
                    )
                    user.set_password(password)
                    user.save()
                    mail_subject = "Confirmar cadastro"
                    mail_message = render_to_string("pages/accounts/notifications/new_account_notify.html", {
                        'domain': get_current_site(self.request),
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'user': user,
                    })
                    to_email = user.email
                    email = EmailMessage(
                        mail_subject,
                        mail_message,
                        config("EMAIL_HOST_USER"),
                        to=[to_email,]
                    )
                    email.send()
                    return redirect('email_notify')
                except ValueError as er:
                    messages.error(self.request, er)
                    return redirect('signup')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return super().dispatch(request, *args, **kwargs)


def new_account_active(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('signup')


class LoginView(FormView):
    template_name = "pages/accounts/signin.html"
    form_class = LoginForm

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = Account.objects.filter(email=email)
        if user.exists():
            auth = authenticate(email=email, password=password)
            if auth:
                login(self.request, auth)
                return redirect('index')
            else:
                messages.error(
                    self.request, 'Cheque seu email, e ative sua conta.')
                return redirect('login')
        else:
            messages.error(
                self.request, 'Dados não conferem. Verifique se os dados enviados estão corretos.')
            return redirect('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return super().dispatch(request, *args, **kwargs)


class LogoutView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('login')


class AccountView(FormView):
    template_name = "pages/accounts/edit_profile.html"
    form_class = AccountForm

    def form_valid(self, form):
        try:
            user = Account.objects.get(id=self.request.user.id)
            user_form = form.save(commit=False)
            user_form.id = user.id
            user_form.save()
            return redirect('account')
        except:
            return redirect('account')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs


class RecoverPasswordView(FormView):
    template_name = "pages/accounts/recover_password.html"
    form_class = RecoverPasswordForm

    def form_valid(self, form):
        """
            Two methods of recover:
            
            1.Moderator method: Is a method used by moderators 
            of the website for recover passwords from users who
            lost your emails or something like that.
            They can use the username only or use the email.
            The moderator will receive  the email, and will generate a new
            password from user.
            2.Common user method: Using

        """
        email = form.cleaned_data['email']
        if self.request.user.is_authenticated:
            if email:
                try:
                    user = Account.objects.get(email=email)
                except:
                    user = Account.objects.get(username=email)

                if user.email == self.request.user.email:
                    mail_subject = "Recuperação de Senha"
                    mail_message = render_to_string("pages/accounts/notifications/recover_password_notify.html", {
                        'domain': get_current_site(self.request),
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'user': user,
                    })
                    to_email = email
                    email = EmailMessage(
                        mail_subject,
                        mail_message,
                        config("EMAIL_HOST_USER"),
                        to=[to_email,]
                    )
                    email.send()
                else:
                    if self.request.user.is_authenticated:
                        if self.request.user.is_superuser:
                            try:
                                user = Account.objects.get(email=email)
                            except:
                                user = Account.objects.get(username=email)
                            mail_subject = "Moderação: Solicitação de recuperação de senha"
                            mail_message = render_to_string("pages/accounts/notifications/moderator_recover_password_notify.html", {
                                'domain': get_current_site(self.request),
                                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                'token': default_token_generator.make_token(user),
                                'user': user,
                                'moderator': self.request.user,
                            })
                            to_email = self.request.user.email
                            email = EmailMessage(
                                mail_subject,
                                mail_message,
                                config("EMAIL_HOST_USER"),
                                to=[to_email,]
                            )
                            email.send()
        else:
            if email:
                try:
                    user = Account.objects.get(email=email)
                    mail_subject = "Recuperação de Senha"
                    mail_message = render_to_string("pages/accounts/notifications/recover_password_notify.html", {
                        'domain': get_current_site(self.request),
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'user': user,
                    })
                    to_email = email
                    email = EmailMessage(
                        mail_subject,
                        mail_message,
                        config("EMAIL_HOST_USER"),
                        to=[to_email,]
                    )
                    email.send()
                except:
                    messages.error(self.request, "Utilizar email válido.")
                    return redirect('recover')       
        return redirect('email_notify')


class NotifyEmailView(TemplateView):
    template_name = "pages/accounts/messages/alert_new_email.html"


def recover_password_decode(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        return redirect('change_password')
    else:
        return redirect('change_password')


class ChangePasswordView(FormView):
    template_name = "pages/accounts/change_password.html"
    form_class = ChangePasswordForm

    def get(self, *args, **kwargs):
        if self.request.session.get('uid'):
            data = {
                'form': ChangePasswordForm(),
            }
            return render(self.request, self.template_name, data)
        else:
            messages.error(
                self.request, 'O link de redefinição de senha é inválido.')
            return redirect('recover')

    def form_valid(self, form):
        password = form.cleaned_data['password']
        confirm_password = form.cleaned_data['confirm_password']
        uid = self.request.session.get('uid')
        if not uid:
            messages.error(
                self.request, 'O link de redefinição de senha é inválido.')
            return redirect('change_password')
        else:
            if password == confirm_password:
                user = Account._default_manager.get(pk=uid)
                user.set_password(password)
                user.save()
                messages.success(self.request, 'Senha alterada com sucesso.')
                return redirect('index')
            else:
                messages.error(self.request, 'Senha não corresponde.')
                return redirect('change_password')

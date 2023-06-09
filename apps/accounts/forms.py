from django import forms

from apps.accounts.models import Account


class NewAccountForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(NewAccountForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs[
                'class'] = 'py-3 outline-blue-500 rounded-md indent-4 bg-gray-100 ring-[1px] ring-gray-500 ring-opacity-40 dark:bg-darkInput dark:text-white'


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'py-3 outline-blue-500 rounded-md indent-4 bg-gray-100 ring-[1px] ring-gray-500 ring-opacity-40 dark:bg-darkInput dark:text-white'

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['email','username','email_notify']

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'py-3 outline-blue-500 rounded-md indent-4 bg-gray-100 ring-[1px] ring-gray-500 ring-opacity-40 dark:bg-darkInput dark:text-white'
            if field == "email_notify":
                self.fields[field].widget.attrs['class'] = ''


class RecoverPasswordForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'py-3 outline-blue-500 rounded-md indent-4 bg-gray-100 ring-[1px] ring-gray-500 ring-opacity-40 dark:bg-darkInput dark:text-white'}))


class ChangePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'py-3 outline-blue-500 rounded-md indent-4 bg-gray-100 ring-[1px] ring-gray-500 ring-opacity-40 dark:bg-darkInput dark:text-white'
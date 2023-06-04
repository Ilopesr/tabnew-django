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
                'class'] = 'py-3 outline-blue-500 rounded-md indent-4 bg-gray-100 ring-[1px] ring-gray-300'


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'py-3 outline-blue-500 rounded-md indent-4 bg-gray-100 ring-[1px] ring-gray-300'

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['email','username','email_notify']

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'py-3 outline-blue-500 rounded-md indent-4 bg-gray-100 ring-[1px] ring-gray-300'


class RecoverPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'py-3 outline-blue-500 rounded-md indent-4 bg-gray-100 ring-[1px] ring-gray-300'}))


class ChangePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'py-3 outline-blue-500 rounded-md indent-4 bg-gray-100 ring-[1px] ring-gray-300'
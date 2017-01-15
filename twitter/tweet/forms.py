from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Textarea, CheckboxSelectMultiple, SelectMultiple, RadioSelect




def validate_login(login):
    if login != 'root':
        raise ValidationError("Login niepoprawny!")

def validate_password(password):
    if password != 'very_secret':
        raise ValidationError("Hasło niepoprawne!")


class Login(forms.Form):
    login = forms.CharField(
        label='Login',
        max_length=64,
        widget=forms.TextInput,
        required=True,
        validators=[validate_login],
    )
    password = forms.CharField(
        label='Password',
        max_length=64,
        widget=forms.PasswordInput,
        required=True,
        validators=[validate_password],
    )
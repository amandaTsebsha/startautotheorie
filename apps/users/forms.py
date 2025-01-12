from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Gebruikersnaam', max_length=150)
    password = forms.CharField(widget=forms.PasswordInput, label='Wachtwoord')
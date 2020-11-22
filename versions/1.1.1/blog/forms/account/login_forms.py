# Django imports
from django import forms


class UserLoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={
            "name": "username", "class": "input100",
            "placeholder": "Username"
        }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
            "name": "password",  "class": "input100",
            "placeholder": "Password"
        }))
from django import forms
from imdbuser.models import BaseUser


class SignUpForm(forms.ModelForm):
    class Meta:
        model = BaseUser
        fields = ['username', 'password', 'display_name', 'user_pic']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)
from django.forms import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm

from .models import UserAccount


class UserAccountCreationForm(UserCreationForm):
    class Meta:
        model = UserAccount
        fields = ["username", "email", "password1", "password2"]


class UserAccountForm(ModelForm):
    class Meta:
        model = UserAccount
        fields = ["avatar", "username", "email", "bio"]

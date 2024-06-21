from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ "username", "email","password"]
        widgets = {
            "password" : forms.widgets.PasswordInput(attrs = {"class" : "hello", "placeholder" : "Enter strong password"})
        }
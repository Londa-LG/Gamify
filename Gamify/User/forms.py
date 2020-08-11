from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class User_Registration(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        widgets = {
            'username': forms.TextInput(attrs={"type":"text", "class":" white-text"}),
            'email': forms.TextInput(attrs={"type":"text"}),
            'password1': forms.TextInput(attrs={"type": "text"}),
            'password2': forms.TextInput(attrs={"type": "text"}),
        }
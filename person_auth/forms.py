from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from .models import Profile

class RegistationForm(UserCreationForm):
    email = forms.EmailField(required=True)
   
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'pic_first', 'department', 'random_sequence']


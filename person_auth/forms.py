from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from .models import Post

class RegistationForm(UserCreationForm):

    # TECH = 1
    # ACOUNING = 2
    # ENVIRO = 3
    # WAREHOUSE = 4
    # QUALITY = 5

    # DEPARTMENT_CHOICE = (
    #     (TECH, 'tech'),
    #     (ACOUNING, 'acounting'),
    #     (ENVIRO, 'enviro'),
    #     (WAREHOUSE, 'warehouse'),
    #     (QUALITY, 'quality')
    # )

    email = forms.EmailField(required=True)
    # department = models.IntegerField(choices=DEPARTMENT_CHOICE, default=TECH)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']
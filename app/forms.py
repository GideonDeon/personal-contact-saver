from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Contact

class UserRegisterForm(UserCreationForm):
   
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
                 
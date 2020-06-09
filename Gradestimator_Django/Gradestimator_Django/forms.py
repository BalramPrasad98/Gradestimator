from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User


class Registration_Form(UserCreationForm):
    class Meta:
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Username"
        self.fields["email"].label = "Email address"
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class EditProfileForm(UserChangeForm):
    template_name=''
    password = None
    
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username']:
            self.fields[fieldname].help_text = None

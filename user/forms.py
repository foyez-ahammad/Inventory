from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2','is_staff', 'is_superuser')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User()
        fields = ('username', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile()
        fields = ('address', 'phone', 'image')

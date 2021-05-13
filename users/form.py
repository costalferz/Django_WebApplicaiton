from django.contrib.auth.models import User
from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

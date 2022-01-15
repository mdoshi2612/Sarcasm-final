from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model=Team
        fields='__all__'

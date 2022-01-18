from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Level

from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model=Team
        fields='__all__'

class LevelForm(forms.Form):
	answer = forms.CharField(label="Answer")
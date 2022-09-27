from django import forms
from .models import WinnerPick


class WinnerPickForm(forms.ModelForm):
    class Meta:
        model = WinnerPick
        fields = ['player','week_number','winningPicks']

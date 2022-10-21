from django import forms
from .models import WinnerPick


class WinnerPickForm(forms.ModelForm):
    class Meta:
        model = WinnerPick
        fields = ['week_number','player','away','home','away_score','home_score','selected_pick','actual_winner','status']




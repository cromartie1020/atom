from django import forms
from .models import Team, Home_Away
from django.db import models


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class HomeAwayForm(forms.ModelForm):
    class Meta:
        model = Home_Away
        fields = ['week_number', 'home_team',
                  'away_team', 'startdate', 'starttime']
        widgets = {'startdate': DateInput(), 'starttime': TimeInput()}


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']

from django.db import models
from datetime import datetime
from django.utils import timezone
from teams import TEAMS 
from players import PLAYERS
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Home_Away(models.Model):
    
    
    week_number = models.IntegerField(default=5)
    
    away_team = models.CharField(max_length=100, choices=TEAMS, default='')
    home_team = models.CharField(max_length=100, choices=TEAMS, default='')
   
    startdate = models.DateField(
        editable=True, null=True, blank=True)
    starttime = models.TimeField(editable=True, null=True, blank=True)

    class Meta:
        ordering = ['week_number','startdate','home_team' ]

    def __str__(self):
        return f'{ self.home_team} and { self.away_team }'

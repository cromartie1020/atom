from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from football.models import Home_Away
User = get_user_model()
team=Home_Away.objects.first()
from teams import TEAMS
from players import PLAYERS
    
STATUS = [
    ("Win","Win"),
    ("Lose","Lose"),
    ("Tie", "Tie")
]
class WinnerPick(models.Model):
    week_number  = models.IntegerField(null=True)

    player       = models.CharField(max_length=200, choices=PLAYERS, null=True)
    away = models.CharField(max_length=200, choices =TEAMS, null= True )
    home = models.CharField(max_length=200, choices =TEAMS, null= True )
    away_score = models.IntegerField(null = True, default=0)    
    home_score = models.IntegerField(null = True, default=0)
    selected_pick  = models.CharField(max_length=250, 
    choices=TEAMS, null = True)
    actual_winner = models.CharField(max_length=250, 
    choices=TEAMS, null = True)
    status = models.CharField(max_length=6, null=True, choices=STATUS)


    def __str__(self):
        return self.selected_pick
    
# Print out the winner selection for the week
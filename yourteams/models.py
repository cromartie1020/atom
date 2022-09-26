from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class WinnerPick(models.Model):
    player       = models.ForeignKey(User, on_delete=models.CASCADE)
    week_number  = models.IntegerField()
    winningPicks = models.CharField(max_length=250)



    

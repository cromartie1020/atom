from django.db import models
from datetime import datetime
from django.utils import timezone


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Home_Away(models.Model):
    TEAMS = [
        ("Arizona Cardinals", 'Arizona Cardinals'),
        ('Atlanta Falcons', 'Atlanta Falcons'),
        ('Baltimore Ravens', 'Baltimore Ravens'),
        ('Buffalo Bills', 'Buffalo Bills'),
        ('Chicago Bears', 'Chicago Bears'),
        ('Carolina Panthers', 'Carolina Panthers'),
        ('Cincinnati Bengals', 'Cincinnati Bengals'),
        ('Cleveland Browns', 'Cleveland Browns'),
        ('Dallas Cowboys', 'Dallas Cowboys'),
        ('Denver Broncos', 'Denver Broncos'),
        ('Detroit lions', 'Detroit lions'),
        ('Green Bay Packers', 'Green Bay Packers'),
        ('Houston Texans', 'Houston Texans'),
        ('Indianapolis Colts', 'Indianapolis Colts'),
        ('Jacksonville Jaguars', 'Jacksonvile Jaguars'),
        ('Kansas City Chiefs', 'Kansas City Chiefs'),
        ('Las Vegas Raiders', 'Las Vegas Raiders'),
        ('Los Angeles Charges', 'Los Angeles Charges'),
        ('Los Angeles Rams', 'Los Angeles Rams'),
        ('Miami Dolphins', 'Miami Dolphins'),
        ('Minnesota Vikings', 'Minnesota Vikings'),
        ('New Orleans Saints', 'New Orleans Saints'),
        ('New England Patriots', 'New England Patriots'),
        ('New York Giants', 'New York Giants'),
        ('New York Jets', 'New York Jets'),
        ('Philadelphia Eagles', 'Philadelphia Eagles'),
        ('Pittsburgh Steelers', 'Pittsburgh Steelers'),
        ('San Francisco 49ers', 'San Francisco 49ers'),
        ('Seatle Seahawks', 'Seatle Seahawks'),
        ('Tampa Bay Buccaneers', 'Tampa Bay Buccaneers'),
        ('Tennessee Titans', 'Tennessee Titans'),
        ('Washington Commanders', 'Washington Commanders'),





    ]
    PLAYERS = [
        ("Mom", "Mom"),
        ("Mr. C.", "Mr. C."),
        ("Tiara", "Tiara"),
        ("Stefaun", "Stefaun")
    ]
    week_number = models.IntegerField(default=4)
    
    away_team = models.CharField(max_length=100, choices=TEAMS, default='')
    home_team = models.CharField(max_length=100, choices=TEAMS, default='')
   
    startdate = models.DateField(
        editable=True, null=True, blank=True)
    starttime = models.TimeField(editable=True, null=True, blank=True)

    class Meta:
        ordering = ['week_number','startdate','home_team' ]

    def __str__(self):
        return f'{ self.home_team} and { self.away_team }'

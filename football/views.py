from django.shortcuts import render, redirect

from .models import Team
from . forms import HomeAwayForm, TeamForm
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from django import forms


class DateTimeForm(forms.Form):

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
        ('los Angeles Rams', 'Los Angeles Rams'),
        ('Miami Dolphins', 'Miami Dolphins'),
        ('Minnesota Vikings', 'Minesota Vikings'),
        ('New Orleans Saints', 'New Orleans Saints'),
        ('New England Patriots', 'New England Patriots'),
        ('New York Giants', 'New York Giants'),
        ('New York Jets', 'New York Jets'),
        ('Philadelphis Eagles', 'Philadelphia Eagles'),
        ('Pittsburgh Steelers', 'Pittsburgh Steelers'),
        ('San Francisco 49ers', 'San Francisco 49ers'),
        ('Seatle Seahawks', 'Seatle Seahawks'),
        ('Tampa Bay Buccaneers', 'Tampa Bay Buccaneers'),
        ('Tennessee Titans', 'Tennessee Titans'),
        ('Washington Football Team', 'Washington Football Team'),





    ]
    week_number = forms.IntegerField()
    home_team = forms.CharField(
        max_length=100, widget=forms.Select(choices='TEAMS'))
    away_team = forms.CharField(
        max_length=100, widget=forms.Select(choices='TEAMS'))
    startdate = forms.DateField(widget=AdminDateWidget())
    starttime = forms.TimeField(widget=AdminTimeWidget())

    class Meta:
        ordering = ['-home_team', '-away_team']

    def __str__(self):
        return f'{ self.home_team} and { self.away_team }'


def home(request):
    teams = Team.objects.all()
    form = DateTimeForm()
    return render(request, 'football/select_teams.html', {'teams': teams, 'form': form})


def home(request):
    teams = Team.objects.all()
    return render(request, 'football/select_teams.html', {'teams': teams})


def teamform(request):
    form = TeamForm(request.POST or None)
    if form.is_valid():
        form.save()

        form = TeamForm()

    return render(request, 'football/team.html', {'form': form})


def list_teams(request):
    teams = list(Team.objects.all())
    form = TeamForm()

    return render(request, 'football/select_teams.html', {'teams': teams, 'form': form})


def homeawayview(request):
    teams = Team.objects.all()
    form = HomeAwayForm(request.POST or None)
    if form.is_valid():
        form.save()
        redirect('homeaway')

    else:
        form = HomeAwayForm()

    return render(request, 'football/select_teams.html', {'form': form, 'teams': teams})


def select_teams(request):
    return render(request, 'football/select_teams.html')

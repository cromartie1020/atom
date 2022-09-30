from django.shortcuts import render, redirect
from .models import Team
from . forms import HomeAwayForm, TeamForm
from django import forms
from django.contrib.auth.models import User


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
        form = HomeAwayForm()
        redirect('homeaway')

    else:
        form = HomeAwayForm()
        print('This is a test.')

    return render(request, 'football/select_teams.html', {'form': form, 'teams': teams})


def select_teams(request):
    return render(request, 'football/select_teams.html')


def testing(request):
    return (request,'testing.html' )
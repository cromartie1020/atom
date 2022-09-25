from django.shortcuts import render
from football.models import Home_Away


def list_home_away(request):
    objects = Home_Away.objects.all()
    return render(request, 'yourteams/select_your_teams.html', {'objects': objects})

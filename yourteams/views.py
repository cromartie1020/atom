from django.shortcuts import render
from football.models import Home_Away


def select_your_picks(request):
    teams = Home_Away.objects.all()
    url=request.build_absolute_uri()
    x=url.index('?')
    x=x+1
    y=url[x:]
    
    print('y: ',y)

    context = {
        'teams':teams,
    
    }
    
        
    return render(request, 'yourteams/select_your_picks.html', context)

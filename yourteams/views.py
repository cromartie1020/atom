from football.models import Team
from django.shortcuts import render, redirect
from football.models import Home_Away
from .models import WinnerPick
from .forms import WinnerPickForm 
from django.contrib.auth import get_user_model
from players import PLAYERS 
user = get_user_model()

def winnerPick(request):
     
    
    form = WinnerPickForm(request.POST or None)
     
    
    if form.is_valid():
        print(request.POST['home'])
        print(request.POST['status'])
        form.save()
        return redirect('winner')
    
    
    context={
        "form":form
    }
    
    return render(request,'yourteams/select_your_picks.html', context)

def select_your_picks(request):
    
    form=WinnerPickForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    
     
    context = {
        
        'form':form
        
    
    }
    
    form=WinnerPickForm()
    
      
    return render(request, 'yourteams/select_your_picks.html', context)


def total(request):
    
    winners=WinnerPick.objects.filter(status='Win').count()

    
    #print(winners.week_number) 
        
    player="Mr. C" 
    context = {
        'winners':winners
    }
    return render(request, 'football/total.html', context)

def print_winners(request):
    
    
    if request.method == 'POST':
        player = request.POST.get('player')
        week_number = request.POST.get('week_number')
        total_points = request.POST.get('total_points')
        total = WinnerPick.objects.filter(week_number__exact=week_number).filter( player__contains=player).filter(status__icontains='Win').count()
        winners = WinnerPick.objects.filter(week_number__exact=week_number).filter( player__contains=player)
       
    
    
        context = {
            "winners":winners,
            "player":player,
            "total":total,
            "total_points":total_points
        }  
        return render(request, 'yourteams/print_winners.html', context)
    
    
    

    return render(request, 'football/final.html')
    

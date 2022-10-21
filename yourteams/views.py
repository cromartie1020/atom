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



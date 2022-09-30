from django.shortcuts import render
from football.models import Home_Away

def select_week(request):
    home_aways=Home_Away.objects.all()
    
    
    context = {
        
        'home_aways':home_aways
    }

    return render (request,'football/select_week.html',context )

def testing(request):
    return render(request,'testing.html')    
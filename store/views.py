from django.shortcuts import render
from football.models import Home_Away

def select_week(request):
    home_aways=Home_Away.objects.all()
    
    
    context = {
        
        'home_aways':home_aways
    }

    return render (request,'football/select_week.html',context )

def testing(request):
    fname=request.GET.get('fname')
    lname=request.GET.get('lname')
    print(fname, lname)
    return render(request,'testing.html')    

    
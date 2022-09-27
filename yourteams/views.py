from django.shortcuts import render
from football.models import Home_Away
from .models import WinnerPick
from .forms import WinnerPickForm 
from django.contrib.auth import get_user_model
user = get_user_model()

def winnerPick(request):
    week_number=1
    context = {
        'week_number':week_number
    }
    return render(request,'yourteams/select_your_picks.html', context)

def select_your_picks(request):
    form=WinnerPickForm()
    print(dir(form))
    teams = Home_Away.objects.all()
    week_number = 1
    print(dir(request))
    user=request.user
    print('user: ',user)
    qd=request.GET
    qd=list(qd)
    x =len(qd)
    
    
    for a in range(0,x):
        print(qd[a])
        w=WinnerPick(player=request.user,week_number=1,winningPicks=qd[0])
        w.save()
        if form.is_valid():
            form.save()

        
    '''
    form=WinnerPickForm()
    if (request.method=="GET" ):
        #print('user: ',user.username)
        url=request.build_absolute_uri()
        print('url: ',url)
    
        x=url.index('?')
        x+=1
        y=url[x:]
        y=y.split('&')
        temp=[]
        
        #player=request.GET['User']
        for z in y:
            z=z.replace('+',' ')
            x=z.index('=')
            z=z[:x]
            print(z)
            #temp=z+temp
            
    '''
     
    context = {
        'teams':teams,
        'week_number':week_number
        
    
    }
    
    
      
    return render(request, 'yourteams/select_your_picks.html', context)

def winnerPick(request):
    pass

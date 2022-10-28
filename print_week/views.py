from django.shortcuts import render

from football.models import Home_Away


def printWeek(request,week_number  ):
    
    home_aways = Home_Away.objects.filter(week_number=week_number).order_by('startdate','starttime')
    #for h_a in home_aways:
    #    print(h_a.away_team,h_a.home_team)
    print(week_number)
    if week_number == 7:
        byes = ['Buffalo,','LA Rams,','Minnesota,','Philadelphia'] 
    if week_number == 6:
        byes = ['Detroit,','Houston,','Las Vegas','Tennessee'] 
            
    else:
        byes=''    
    context = {
        'home_aways':home_aways,
        'week_number':week_number,
         
        'byes':byes


    } 
    
           

    return render (request,'print_week/print_week.html', context)
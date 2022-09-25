from django.shortcuts import render

from football.models import Home_Away


def printWeek(request,week_number  ):
    home_aways = Home_Away.objects.filter(week_number=week_number).order_by('startdate','starttime')
    
    context = {
        'home_aways':home_aways,
        'week_number':week_number

    } 
    
           

    return render (request,'print_week/print_week.html', context)
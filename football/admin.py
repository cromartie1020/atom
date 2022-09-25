from django.contrib import admin

from .models import Team, Home_Away

class Home_Away_Form(admin.ModelAdmin):
    list_display = ['week_number','startdate','away_team','home_team', 'starttime']
    

admin.site.register(Team)
admin.site.register(Home_Away, Home_Away_Form)

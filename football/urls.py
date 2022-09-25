from django.urls import path
from . import views

urlpatterns = [

    path('form/', views.teamform, name='team'),
    path('', views.homeawayview, name='homeaway'),
    #path('list/', views.list_teams, name='list_teams'),
    #path('selectteams/', views.select_teams, name='select_teams'),
]

from django.urls import path
from . import views

urlpatterns = [

    path('form/', views.teamform, name='team'),
    path('', views.homeawayview, name='homeaway'),
    path('final/', views.print_final, name='final'),
    
   
    
]

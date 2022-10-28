from django.urls import path
from . import views
urlpatterns = [
    path('', views.select_your_picks, name='picks'),
    path('winner/', views.winnerPick, name='winner'),
    path('total/',views.total, name='total'),
    #path('winners/<str:player>/<int:week_number>/', views.print_winners, name='print_winners')
    path('winners/', views.print_winners, name='print_winners'),
    #path('winners_final/',views.print_winners_final,name='print_winners_final')
]

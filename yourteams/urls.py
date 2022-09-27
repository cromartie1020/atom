from django.urls import path
from . import views
urlpatterns = [
    path('', views.select_your_picks, name='picks'),
    path('winner/', views.winnerPick, name='winner'),
]

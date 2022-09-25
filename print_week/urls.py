from django.urls import path
from .views import printWeek
urlpatterns =[
    path('<int:week_number>/',printWeek, name='print_week'),

]
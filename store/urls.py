from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.select_week, name='select_week'),
    path('testing/',views.testing),
    path('select/', include('football.urls')),
    path('print_week/',include('print_week.urls')),
    path('teams/', include('yourteams.urls')),
    path('yourteams/',include('yourteams.urls')),
    path('account/', include('allauth.urls')),

    path('admin/', admin.site.urls),
    #path('test/',views.test,name='test')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

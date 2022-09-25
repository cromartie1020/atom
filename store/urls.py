from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.select_week, name='select_week'),
    path('select/', include('football.urls')),
    path('print_week/',include('print_week.urls')),
    path('teams/', include('yourteams.urls')),
    path('accounts/', include('allauth.urls')),

    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

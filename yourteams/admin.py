from asyncio.proactor_events import _ProactorBaseWritePipeTransport
from django.contrib import admin
from .models import WinnerPick

class RegisterAdmin(admin.ModelAdmin):
    list_display = ['player','week_number','away','home','away_score','home_score','selected_pick','actual_winner','status']
       


admin.site.register(WinnerPick, RegisterAdmin)

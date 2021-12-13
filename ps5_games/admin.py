from django.contrib import admin
from .models import Ps5_games


@admin.register(Ps5_games)
class Ps5_gamesAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'updated', 'author', 'published']
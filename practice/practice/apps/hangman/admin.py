from django.contrib import admin
from .models import Game


@admin.register(Game)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['word', 'guessed_letters', 'max_attempts', 'attempts_left']

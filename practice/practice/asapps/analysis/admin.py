from django.contrib import admin
from .models import Tabs

@admin.register(Tabs)
class TabsAdmin(admin.ModelAdmin):
    list_display = ['tab_name', 'saved_btn']


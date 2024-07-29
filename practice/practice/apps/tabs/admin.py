from django.contrib import admin
from. models import Tab

@admin.register(Tab)
class TabDataAdmin(admin.ModelAdmin):
    list_display = ['id','city_name', 'title', 'description', 'color', 'saved_btn']


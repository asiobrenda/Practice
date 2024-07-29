from django.contrib import admin
from .models import Topic, Languages, News, Comments


@admin.register(Languages)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'lang_name']



@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['id','lang', 'title', 'text', 'date']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'text', 'date']

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'text', 'news']


from django.contrib.auth.admin import UserAdmin
from. forms import SignUpCreationForm
from.models import (SignUpUser, Home, Biography, Skills, Services, Portfolio, Testimonial, Contact)
from django.contrib import admin
class SignUpUserAdmin(UserAdmin):
      add_form = SignUpCreationForm
      model = SignUpUser
      list_display = ['username', 'email']


admin.site.register(SignUpUser, SignUpUserAdmin)



@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['background_image', 'front_text', 'middle_text', 'last_text']

@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    list_display = ['name', 'profile', 'email', 'phone', 'image']

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'percentage']

@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id','image','service', 'description']

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id','image','header_four', 'italics', 'category']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['description','image','name', 'title']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email', 'subject', 'message']
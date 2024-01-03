from django.urls import path
from.views import index, contact, sign_up, truncate_skills
from django.contrib.auth.views import (LoginView, LogoutView)
from. import views


app_name = "brenda"

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='Contact'),
    path('signUp/', sign_up, name = 'SignUp'),
    path('login/', LoginView.as_view(template_name='brenda/login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='brenda/logout.html'),name='logout'),
    path('truncate/<str:table_name>/', truncate_skills, name='truncate_table'),
    # path('bio/', bio, name='bio'),
    # path('skill/', skill, name='skill')
]


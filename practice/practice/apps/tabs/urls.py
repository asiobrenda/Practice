from django.urls import path
from .views import home, get_tab_name

app_name = 'tabs'

urlpatterns = [
    path('', home, name='home'),
    path('get_tab_name',get_tab_name, name='get_tab_name')

]
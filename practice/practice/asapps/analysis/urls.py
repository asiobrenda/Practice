from django.urls import path
from .import views

app_name = 'analysis'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_tab', views.add_tab, name='add_tab'),
    path('get_data', views.get_data, name='get_data'),
    path('delete_tab', views.delete_tab, name='delete_tab'),
    path('add_btn', views.add_btn, name='add_btn'),
    path('get_add_btn', views.get_add_btn, name='get_add_btn'),
    path('delete_sub_tab_', views.delete_sub_tab_, name='delete_sub_tab_'),
    path('get_next_btn_id/', views.get_next_btn_id, name='get_next_btn_id'),
    path('cloned_btn/', views.cloned_btn, name='cloned_btn'),
    path('get_cloned_btn/', views.get_cloned_btn, name='get_cloned_btn'),
    path('get_cloned_data/', views.get_cloned_data, name='get_cloned_data'),
]
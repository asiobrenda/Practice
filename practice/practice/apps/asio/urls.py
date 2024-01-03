from django.urls import path
from .views import home, load_data

app_name = 'asio'


urlpatterns = [
    path('', home, name='home'),
    path('load_data/', load_data, name='load-data'),
    # path('get_data/', get_data, name='get-data'),
]

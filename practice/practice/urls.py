"""practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('practice.apps.brenda.urls')),
    path('a/', include('practice.apps.asio.urls')),
    path('c/', include('practice.apps.core.urls')),
    path('t/', include('practice.apps.tabs.urls')),
    path('f/', include('practice.apps.foodapp.urls')),
    path('b/', include('practice.apps.blog.urls')),
    path('h/', include('practice.apps.hangman.urls')),
    path('bk/', include('practice.apps.banking.urls')),
    path('l/', include('practice.apps.loans.urls')),
    path('d/', include('practice.asapps.analysis.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.autodiscover()
admin.site.enable_nav_sidebar = False
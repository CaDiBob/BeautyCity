"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

from . import settings
from beauty_salon import views
from users.views import login_or_register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_index, name='index'),
    path('service/', render, kwargs={'template_name': 'service.html'}, name='service'),
    path('service/reservation', render, kwargs={'template_name': 'reservation.html'}, name='reservation'),
    path('accounts/profile/', render, kwargs={'template_name': 'profile.html'}, name='profile'),
    path('accounts/login/', render, kwargs={'template_name': 'service.html'}, name='login'),
    path('login/', login_or_register, name='login_or_register'),
    path('__debug__/', include('debug_toolbar.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

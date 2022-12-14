from django.urls import path

from .views import LoginMobile

app_name = "beauty_salon"

urlpatterns = [
    path('login_mobile/', LoginMobile.as_view(), name='login_mobile'),
]

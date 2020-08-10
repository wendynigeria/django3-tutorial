from django.urls import path
from . import views

# code below here

urlpatterns = [
    path('', views.home, name='home'),
    path('password', views.password, name='password'),
]
from django.urls import path, include
from . import views

app_name = 'custom_forms'

urlpatterns = [
    path('', views.home, name='home'),
]

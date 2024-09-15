from django.urls import path, include
from . import views

app_name = 'editables_temp'

urlpatterns = [
    path('', views.home, name='home'),
]

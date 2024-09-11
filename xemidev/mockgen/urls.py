from django.urls import path, include
from . import views

app_name = 'mockgen'

urlpatterns = [
    path('',views.mock_gen,name='generator'),
    
]
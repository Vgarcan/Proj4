from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('faq/',views.faq,name='faq'),
    path('pricing/',views.pricing,name='pricing'),
    path('terms/',views.terms,name='terms'),
]

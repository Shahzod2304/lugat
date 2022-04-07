from django.urls import path 
from .views import *

urlpatterns = [
    path('', HomePage, name='home'),
    path('about/', AboutPage, name='about'),
    path('contactus/', ContactUs, name='contactus'),
]
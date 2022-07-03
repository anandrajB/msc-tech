from django.urls import path

from .fviews import home , index , mode , register , profile

urlpatterns = [
    path('',index),
    path('home',home),
    path('selectmode',mode),
    path('register',register),
    path('profile',profile)
]

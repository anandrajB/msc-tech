from django.urls import path

from .fviews import home , index , mode , register , piston , table

urlpatterns = [
    path('',index),
    path('home',home),
    path('selectmode',mode),
    path('register',register),
    path('piston',piston),
    path('table',table)
]

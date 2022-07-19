from django.urls import path

from .fviews import home , index , mode , register , piston , table ,home2 , overview

urlpatterns = [
    path('',index),
    path('guide',home),
    path('expert',home2),
    path('selectmode',mode),
    path('register',register),
    path('piston',piston),
    path('table',table),
    path('overview',overview)
]

from django.urls import path

from accounts.fviews import index
from .views import UserLoginView , UserProfileApiView, UserSignUpApiView , logoutapi , NameListCreateapi
from .fviews import home  , mode , register , profile 

urlpatterns = [
    path('login/',UserLoginView.as_view()),
    path('logout/',logoutapi.as_view()),
    path('profile/',UserProfileApiView.as_view()),
    path('signup/',UserSignUpApiView.as_view()),
    path('core/names/',NameListCreateapi.as_view()),
    path('home',home),
    path('selectmode',mode),
    path('register',register),
    path('profile',profile),
]

from django.urls import path

from accounts.fviews import index
from .views import UserLoginView , UserProfileApiView, UserSignUpApiView , logoutapi , NameListCreateapi , ScoreCreateApiview

urlpatterns = [
    path('login/',UserLoginView.as_view()),
    path('logout/',logoutapi.as_view()),
    path('profile/',UserProfileApiView.as_view()),
    path('signup/',UserSignUpApiView.as_view()),
    path('parts/',NameListCreateapi.as_view()),
    path('score/',ScoreCreateApiview.as_view()),    
]

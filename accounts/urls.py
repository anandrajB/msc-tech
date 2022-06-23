from django.urls import path
from .views import UserLoginView , UserProfileApiView, UserSignUpApiView , logoutapi , NameListCreateapi

urlpatterns = [
    path('login/',UserLoginView.as_view()),
    path('logout/',logoutapi.as_view()),
    path('profile/',UserProfileApiView.as_view()),
    path('signup/',UserSignUpApiView.as_view()),
    path('core/names/',NameListCreateapi.as_view())
]

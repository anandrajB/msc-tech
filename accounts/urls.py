from django.urls import path

from accounts.fviews import index
from .views import SparesApi, UserLoginView , UserProfileApiView, UserSignUpApiView , logoutapi , NameListCreateapi 

urlpatterns = [
    path('login/',UserLoginView.as_view()),
    path('logout/',logoutapi.as_view()),
    path('profile/',UserProfileApiView.as_view()),
    path('signup/',UserSignUpApiView.as_view()),
    path('parts/',NameListCreateapi.as_view()),  
    path('spares/',SparesApi.as_view())
]

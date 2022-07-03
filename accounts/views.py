from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    ListCreateAPIView
)
from django.contrib.auth.models import User
from django.contrib.auth import (
    get_user_model,
    authenticate,
    login,
    logout
)
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from accounts.models import Names
from .serializer import Loginserialzier, Namesserializer, UserSerializer, profileserializer
from rest_framework.permissions import AllowAny , IsAuthenticated
# Create your views here.
User = get_user_model()


class UserLoginView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Loginserialzier
    permission_classes = [AllowAny]


    def post(self, request):
        username = request.data.get('username',None)
        password = request.data.get("password", None)
        
        if username and password:
            user = authenticate(username=username,password=password)
            if user:
                    login(request, user)
                    token, created = Token.objects.get_or_create(user=user)
                    data = {
                        "user_id": user.id,
                        "username" :  user.username,
                        "first_name" : user.first_name,
                        "email" : user.email,
                        'token' : token.key,
                        "is_superuser" : user.is_superuser,
                    }
                    return Response({"status": "success", "data": data }, status=status.HTTP_200_OK)
            return Response(
                {"status": "failure", "data": "Unable to login with given credentials"} , status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
            )
        return Response(
            {
                "status": "failure",
                "data": "You need to provide both phone and email",
            }, status=status.HTTP_204_NO_CONTENT
        )




class UserProfileApiView(ListAPIView):
    queryset = User.objects.all()
    serilizer_class = profileserializer
    permission_classes = [IsAuthenticated]

    def list(self,request):
        user = request.user
        query = User.objects.filter(id = user.id)
        serializer = profileserializer(query,many=True)
        return Response({"status": "success", "data": serializer.data},status=status.HTTP_200_OK)



class UserSignUpApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)
        return Response({"status": "failure", "data": serializer.errors},status=status.HTTP_204_NO_CONTENT)


class logoutapi(APIView):
    premission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"status": "logout success"}, status=status.HTTP_200_OK)



class NameListCreateapi(ListCreateAPIView):
    queryset = Names.objects.all()
    serializer_class = Namesserializer
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user
        query = Names.objects.filter(user = user.id)
        serializer = Namesserializer(query,many=True)
        return Response({"status": "success", "data": serializer.data},status=status.HTTP_200_OK)



    def post(self, request):
        user = request.user
        serializer = Namesserializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = user)
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)
        return Response({"status": "failure", "data": serializer.errors},status=status.HTTP_204_NO_CONTENT)

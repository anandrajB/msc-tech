from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Names


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField()
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')



class profileserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id' ,'username' , 'email' , 'first_name' , 'last_name','is_superuser','last_login','date_joined']


class Loginserialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']


class Namesserializer(serializers.ModelSerializer):
    class Meta:
        model = Names
        fields = '__all__'
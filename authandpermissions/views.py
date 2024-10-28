from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import Authserializer, Loginserializer
from .models import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import  IsAuthenticated

# Create your views here.
class Authapi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = Authoriseuser.objects.all()
        get_serializer = Authserializer(queryset, many = True)
        return Response({
            'data':get_serializer.data,
            'status' : status.HTTP_200_OK
            })
    
class Login(APIView):
    def post(self, request):
        data = request.data
        serializer = Loginserializer(data = data)
        if not serializer.is_valid():
            return Response(
            {
                "data" : serializer.errors,
                'status' : status.HTTP_401_UNAUTHORIZED
            }
            )   

        username = serializer.data['username']
        password = serializer.data['password']

        auth_obj = authenticate(username = username, password= password)
        if auth_obj:
            token = Token.objects.get_or_create(user = auth_obj)
            return Response(
            {
                "Token" : str(token),
                'status' : status.HTTP_200_OK
            }
        )    

        return Response(
            {
                "data" : " ",
                'status' : status.HTTP_401_UNAUTHORIZED
            }
        )    
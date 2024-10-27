from django.shortcuts import render
from .serializers import Blogserializer, Commentserializer
from rest_framework import generics
from .models import Blog, Comment


# Nested serializers (Commentserializer inside a blogserializer)
class Blogview(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blogserializer

class Commentview(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = Commentserializer  

class Blogdetailsview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blogserializer
    lookup_field = "pk"

class Commentdetailsview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = Commentserializer
    lookup_field = "pk"
from django.shortcuts import render
from .serializers import Blogserializer, Commentserializer
from rest_framework import generics
from .models import Blog, Comment
from rest_framework.filters import SearchFilter, OrderingFilter


# Nested serializers (Commentserializer inside a blogserializer)
class Blogview(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blogserializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['blog_body', 'blog_title']
    # Starts with particular text
    #search_fields = ['^blog_body']

    # Ordering filter
    ordering_fields = ["id"]


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
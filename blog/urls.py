from django.urls import path
from .views import *

urlpatterns = [
    path("blogs/", Blogview.as_view()),
    path('comments/', Commentview.as_view()),

    path("blogs/<int:pk>/", Blogdetailsview.as_view()),
    path("comments/<int:pk>", Commentdetailsview.as_view())
] 
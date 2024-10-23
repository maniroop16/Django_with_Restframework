from restapi.views import *
from django.urls import path

urlpatterns = [
    path("students/", students)
]
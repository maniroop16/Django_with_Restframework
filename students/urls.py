from students.views import *
from django.urls import path

urlpatterns =[
    path("", students, name = "students")
]


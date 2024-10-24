from django.urls import path
from restapi.views import *


urlpatterns = [
    path("employee/", Employees.as_view()),
    path("employee/<int:pk>", Employeesdetails.as_view()),
]
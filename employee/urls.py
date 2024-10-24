from django.urls import path
from restapi.views import *


urlpatterns = [
    path("employee/", Employees.as_view()),
    path("employee/<int:id>", Employeesdetails.as_view()),
]
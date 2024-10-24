from django.urls import path, include
from restapi.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("employee", Employees, basename="employees")


urlpatterns = [
#    path("employee/", Employees.as_view()),
#    path("employee/<int:pk>", Employeesdetails.as_view()),

    path("", include(router.urls))
]
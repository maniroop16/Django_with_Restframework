from django.urls import path
from .views import Authapi, Login

urlpatterns = [
    path("authcheck/", Authapi.as_view()),
    path('login/', Login.as_view())
]
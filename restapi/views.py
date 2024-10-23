from django.shortcuts import render
from django.http import JsonResponse

def students(request):
    students = {
        "name":"sai",
        "age":24
    }
    return JsonResponse(students)

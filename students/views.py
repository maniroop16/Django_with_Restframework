from django.shortcuts import render
from django.http import HttpResponse

def students(request):
    students = [{
        "name":"sai",
        "age":24,
        "profession":"Software"
    }]
    return HttpResponse(students)

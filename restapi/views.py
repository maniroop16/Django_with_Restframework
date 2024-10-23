from django.shortcuts import render
from django.http import JsonResponse
from students.models import Students
from restapi.serializers import Studentserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


#Function-Based-View
@api_view(["GET","POST"])
def students(request):
    if request.method == "GET":
        students = Students.objects.all()
        students_serializer = Studentserializer(students, many = True)
        return Response(students_serializer.data,status = status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer = Studentserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])    
def getstudentbyid(request, id):
    try:
        student = Students.objects.get(id = id)
    except Students.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        student_get_serializer = Studentserializer(student)
        return Response(student_get_serializer.data, status=status.HTTP_200_OK) 
    elif request.method == "PUT":
        update_serializer = Studentserializer(student,data = request.data)
        if update_serializer.is_valid():
            update_serializer.save()
            return Response(update_serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
          

'''    # Serializing in below way is not advisable
    students = Students.objects.all()
    stud_list = list(students.values())
    return JsonResponse(stud_list, safe=False)'''

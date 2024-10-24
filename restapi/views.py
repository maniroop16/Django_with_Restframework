from django.shortcuts import render
from django.http import JsonResponse
from students.models import Students
from restapi.serializers import Studentserializer, Employeeserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from employee.models import Employee
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins,generics



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


#Class-Based-Views
'''class Employees(APIView):
    def get(self, request):
        all_employees = Employee.objects.all()
        serilize_employee = Employeeserializer(all_employees, many = True)
        return Response(serilize_employee.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = Employeeserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_404_NOT_FOUND)
    
class Employeesdetails(APIView):
    def get_object(self, id):
        try:
            return Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            raise Http404
        
    def get(self,request,id):
        employee_by_id = self.get_object(id)
        id_serilizer = Employeeserializer(employee_by_id)
        return Response(id_serilizer.data, status = status.HTTP_200_OK)    
    
    def put(self,request,id):
        edit_employee = self.get_object(id)
        edit_serilize = Employeeserializer(edit_employee, data=request.data)
        if edit_serilize.is_valid():
            edit_serilize.save()
            return Response(edit_serilize.data, status = status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        del_employee = self.get_object(id)
        del_employee.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)'''


class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class Employeesdetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
        
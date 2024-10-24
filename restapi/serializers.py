from rest_framework.serializers import ModelSerializer
from students.models import Students
from employee.models import Employee


class Studentserializer(ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"


class Employeeserializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


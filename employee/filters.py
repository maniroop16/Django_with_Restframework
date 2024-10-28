import django_filters 
from .models import Employee

class Employeefilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name="designation", lookup_expr="iexact")
    emp_name = django_filters.CharFilter(field_name="emp_name", lookup_expr="icontains")

    id_min = django_filters.CharFilter(method="filterby_empid", label="From Emp Id")
    id_max = django_filters.CharFilter(method="filterby_empid", label="To Emp Id")

    class Meta:
        model = Employee
        fields = ["designation", "emp_name", "id_max", "id_min"]

    def filterby_empid(self, queryset, name, value):
        if name == "id_min":
            return queryset.filter(emp_id__gte = value)
        elif name == "id_max":
            return queryset.filter(emp_id__lte = value)
        return queryset

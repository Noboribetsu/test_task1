from rest_framework import generics
from employees.models import EmployeesList
from employees.API import serializers


class EmployeeList(generics.ListCreateAPIView):
    queryset = EmployeesList.objects.all().order_by('id')
    serializer_class = serializers.EmployeeSerializer


class EmployeeRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeesList.objects.all().order_by('id')
    serializer_class = serializers.EmployeeSerializer

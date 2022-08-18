from employees.models import EmployeesList
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeesList
        fields = [
            'id',
            'fullname',
            'position',
            'salary',
            'employment_date',
            'supervisor',
            'subordinates'
        ]

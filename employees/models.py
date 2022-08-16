from django.db import models


class EmployeesList(models.Model):
    fullname = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    employment_date = models.DateField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    supervisor = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True, related_name='subordinates')

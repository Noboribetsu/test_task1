from employees.API.views import EmployeeList, EmployeeRetrieve
from django.urls import path

urlpatterns = [
    path('employees/', EmployeeList.as_view()),
    path('employees/<int:pk>', EmployeeRetrieve.as_view()),
]

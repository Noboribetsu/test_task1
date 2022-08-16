from django.views.generic import ListView

from .models import EmployeesList


class EmployeesHierarchy(ListView):
    model = EmployeesList
    template_name = 'index.html'
    queryset = EmployeesList.objects.filter(supervisor=None).order_by('id')
    paginate_by = 5

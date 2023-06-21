from django.shortcuts import render
from .models import * 
from django.views.generic import ListView,DetailView,CreateView,UpdateView

# Create your views here.
class Home(CreateView):
    model=Employee
    fields='__all__'

class EmployeeList(ListView):
    model=Employee
    context_object_name='Employees'
    ordering=['name']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_count'] = self.model.objects.count()
        return context

class EmployeeDetail(DetailView):
    model=Employee
    context_object_name='Emp'

class EmployeeCreate(CreateView):
    model=Employee
    fields='__all__'

class EmployeeUpdate(UpdateView):
    model=Employee
    fields='__all__'


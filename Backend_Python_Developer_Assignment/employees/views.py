from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Employee
from .forms import EmployeeForm
from django.urls import reverse

from django.views.generic import(
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
    )

# Class based views 

class EmployeesListView(ListView):
    template_name = 'employees/employees_list.html'
    queryset = Employee.undeleted_objects.all()
    paginate_by = 6
    model = Employee

class FormerEmployeesListView(ListView):
    template_name = 'employees/former_employees_list.html'
    queryset = Employee.objects.filter(is_deleted = True).all()
    paginate_by = 5
    model = Employee



class EmployeeCreateView(CreateView):
    template_name = 'employees/employee_create.html'
    form_class = EmployeeForm
    queryset = Employee.objects.all()
    def get_success_url(self):
        return reverse('employee_create')



class EmployeeDetailView(DetailView):
    template_name = 'employees/employee_detail.html'
    queryset = Employee.objects.all()

class FormerEmployeeDetailView(DetailView):
    template_name = 'employees/former_employee_detail.html'
    queryset = Employee.objects.filter(is_deleted = True).all()
    



class EmployeeDeleteView(DeleteView):
    template_name = 'employees/employee_delete.html'
    form_class = EmployeeForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Employee, id = id_)
        
    def get_success_url(self):
        return reverse('employees_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.soft_delete()
        return HttpResponseRedirect(self.get_success_url())


class FormerEmployeeDeleteView(DeleteView):
    template_name = 'employees/former_employee_delete.html'
    form_class = EmployeeForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Employee, id = id_)
        
    def get_success_url(self):
        return reverse('former_employees_list')




class EmployeeUpdateView(UpdateView):
    template_name = 'employees/employee_update.html'
    form_class = EmployeeForm
    queryset = Employee.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Employee, id = id_)
    
    def get_success_url(self):
        return reverse('employees_list')


class FormerEmployeeUpdateView(UpdateView):
    template_name = 'employees/employee_update.html'
    form_class = EmployeeForm
    queryset = Employee.objects.filter(is_deleted = True).all()
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Employee, id = id_)
    
    def get_success_url(self):
        return reverse('former_employees_list')




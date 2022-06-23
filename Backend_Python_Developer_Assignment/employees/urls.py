"""company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .import views

urlpatterns = [
    path('', views.EmployeesListView.as_view(), name='employees_list'),
    path('create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('<int:id>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    path('<int:id>/update/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('former/', views.FormerEmployeesListView.as_view(), name='former_employees_list'),
    path('former/<int:pk>/', views.FormerEmployeeDetailView.as_view(), name='employee_detail'),
    path('former/<int:id>/delete/', views.FormerEmployeeDeleteView.as_view(), name='employee_delete'),
    path('former/<int:id>/update/', views.FormerEmployeeUpdateView.as_view(), name='employee_update'),
    
]
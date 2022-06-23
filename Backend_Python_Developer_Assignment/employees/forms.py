from django import forms
from .models import Employee
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'name',
            'email_adress',
            'phone_number',
            'home_adress',
            'date_of_employment',
            'date_of_birth'
            ]
        widgets = {
            'name' : forms.TextInput(attrs={'blank' : 'True'}),                              
            'phone_number' : PhoneNumberPrefixWidget(initial='BA'),
            'date_of_employment' : forms.TextInput(attrs={'placeholder':'mm/dd/yyyy'}),
            'date_of_birth' : forms.TextInput(attrs={'placeholder':'mm/dd/yyyy'}),
            }
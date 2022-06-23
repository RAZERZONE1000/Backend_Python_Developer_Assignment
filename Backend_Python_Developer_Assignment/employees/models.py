from django.db import models

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class SoftDeleteManager(models.Manager):
    
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)



class SoftDeleteEmployee(models.Model):

    is_deleted = models.BooleanField(default=False)
    objects = models.Manager()
    undeleted_objects = SoftDeleteManager()
    
    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True



class Employee(SoftDeleteEmployee):

    name                = models.CharField(max_length=50)
    email_adress        = models.EmailField(max_length=150)
    phone_number        = PhoneNumberField()
    home_adress         = models.CharField(max_length=100) 
    date_of_employment  = models.DateField()
    date_of_birth       = models.DateField()

    def get_absolute_url(self):
        return '/employees/' 

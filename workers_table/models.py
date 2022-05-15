from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Department(models.Model):
    '''
    Department
    args: name: CharField(), phone: PhoneNumberField() 
    '''
    name = models.CharField(verbose_name="department_name", blank=False, max_length=50)
    phone = PhoneNumberField()

    def __str__(self):
        return self.name

class Position(models.Model):
    '''
    Position
    args: name: CharField() 
    '''
    name = models.CharField(verbose_name="position_name", blank=False, max_length=50)
    
    def __str__(self):
        return self.name

class Employee(User):
    '''
    Employee
    args: username: CharField(), phone: PhoneNumberField(),
    email, password, 
    department: Department ID, position: Position ID,
    '''
    phone = PhoneNumberField()
    department = models.ForeignKey(Department, related_name="employee", on_delete=models.DO_NOTHING)
    position = models.ForeignKey(Position, related_name="position",on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.first_name} {self.last_name}' 

class DepartmentHead(models.Model):
    '''
    DepartmentHead
    args: head: Employee ID, department: Department ID 
    '''
    # Employee
    head = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="department_head", verbose_name="head", on_delete=models.CASCADE, blank=False)
    department = models.ForeignKey(Department, related_name="department_head", on_delete=models.CASCADE, blank=False)

class EmployeeStatusChoices(models.TextChoices):
    '''Status of employee movement'''

    ARRIVED = "ARRIVED", "Прибыл"
    LEFT = "LEFT", "Убыл"


class Control(models.Model):
    '''
    Registration of employee movement
    date: that date
    time: register time
    status: status of employee movement
    '''
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="control", on_delete=models.DO_NOTHING, blank=False)
    date = models.DateField(verbose_name="date", auto_now_add=True, blank=False)
    time = models.TimeField(verbose_name="time", auto_now_add=True,blank=False)
    status = models.TextField(
        choices=EmployeeStatusChoices.choices,
        default=EmployeeStatusChoices.ARRIVED
        )
    reason = models.TextField(default='')

class Exceptions(models.Model):
    '''
    News about time changing in schedule
    date: that date is exception
    time: how long would it be
    name: reason for exception
    '''
    date = models.DateField(verbose_name="date", auto_now_add=True, blank=False, unique=True)
    time = models.TimeField(verbose_name="time", auto_now_add=True,blank=False)
    name = models.TextField(default='', blank=False)

class Vacation(models.Model):
    '''
    Vacation days of employee
    employee: id of employee
    start_date: first day off
    end_date: last day_off
    '''
    # Employee
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="vacation", on_delete= models.CASCADE)
    start_date = models.DateField(verbose_name="start_date", auto_now_add=True, blank=False)
    end_date = models.DateField(verbose_name="end_date", auto_now_add=True, blank=False)


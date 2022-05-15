
# Create your views here.
import datetime
from django.http import HttpResponse

from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, login

from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters import rest_framework as filters

from workers_table.forms import LoginForm
from workers_table.models import Employee, Control
from workers_table.permissions import ControlPermission
from workers_table.serializers import ControlSerializer, EmployeeSerializer

import requests

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('homepage')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'workers_table/login.html', {'form': form})
    
def logout(request):
    auth_logout(request)
    return redirect('login')

def workers(request):
    '''
    returns the table of employees and their current status of being at work
    '''
    if request.user.is_authenticated:
        token = Token.objects.get(user=request.user)
        headers = {
            'accept': 'application/json' ,
            'authorization': f'Token {token}'
        }
        employees = requests.get('http://127.0.0.1:8000/api/today/', headers=headers).json()
        content = {
        "employees": employees
        }
        return render(request,"workers_table/index.html", content)
    return redirect('login')
    

def homepage(request, user=None):
    if not request.user.is_authenticated:
        return redirect('login')
    content = {
        "user": request.user
    }
    return render(request,"workers_table/homepage.html", content)

def employee_page(request):
    employee_id = request.GET.get('id', None)
    user = request.user
    print(user)
    if user == None:
        return HttpResponse('Вы не авторизованы')
    elif employee_id == None:
        return HttpResponse('У данного сотрудника нет id')
    else:
        token = Token.objects.get(user=request.user)
        headers = {
            'accept': 'application/json' ,
            'authorization': f'Token {token}'
        }
        responce = requests.get(f'http://127.0.0.1:8000/api/employees/{employee_id}/', headers=headers).json()
        print(responce)
        context = {
            "employee": responce,
        }
        return render(request, "workers_table/employee.html", context)
    


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.DjangoFilterBackend]
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        Token.objects.create(user=self)
        serializer.save()

class ControlViewSet(ModelViewSet):
    queryset = Control.objects.all()
    serializer_class = ControlSerializer
    filter_backends = [filters.DjangoFilterBackend]
    permission_classes = [IsAdminUser, ControlPermission]

class ControlThatDayViewSet(ModelViewSet):
    # employees who left
    queryset_left = Control.objects\
        .filter(date=datetime.date.today(), status="LEFT")
    # empolees who arrived today and haven't left
    queryset_arrived = Control.objects\
        .filter(date=datetime.date.today(), status="ARRIVED")\
        .exclude(employee__in=queryset_left.values_list("employee"))
    queryset = queryset_left.union(queryset_arrived)
    # queryset_absent = Employee.objects.exclude(id__in=queryset.values_list("employee"))
    serializer_class = ControlSerializer
    filter_backends = [filters.DjangoFilterBackend]
    permission_classes = [IsAuthenticated]

def post_control(request):
    if request.user.is_authenticated:
        token = Token.objects.get(user=request.user)
        status_repeat = 0
        status_repeat = Control.objects.filter(employee_id=request.POST["employee_id"],
            status=request.POST["status"], date=datetime.date.today()).count()
        print(status_repeat)
        if status_repeat != 0:
            return HttpResponse('Вы не можете выбрать данный статус')  
        employee = Control(employee_id=request.POST["employee_id"],
            status=request.POST["status"],reason=request.POST["reason"]).save()
        
        return redirect("list")

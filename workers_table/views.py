
# подключение модулей
import datetime
import requests

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

# аутентификация пользователя
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

# выход из аккаунта
def logout(request):
    auth_logout(request)
    return redirect('login')

# функция, которая выводит данные на странице "Таблица сотрудников" 
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
        
        employees = requests.get(f'http://{request.get_host()}/api/today/', headers=headers).json()
        content = {
        "employees": employees
        }
        return render(request,"workers_table/index.html", content)
    return redirect('login')
    
# страница регистрации сотрудника
def homepage(request, user=None):
    if not request.user.is_authenticated:
        return redirect('login')
    content = {
        "user": request.user
    }
    return render(request,"workers_table/homepage.html", content)

# функция, котрая выводит подробную информацию о сотруднике
def employee_page(request):
    if request.user.is_authenticated:
        employee_id = request.GET.get('id', None)
        user = request.user
        if employee_id == None:
            return HttpResponse('У данного сотрудника нет id')
        else:
            token = Token.objects.get(user=request.user)
            headers = {
                'accept': 'application/json' ,
                'authorization': f'Token {token}'
            }
            responce = requests.get(f'http://{request.get_host()}/api/employees/{employee_id}/', headers=headers).json()
            print(responce)
            context = {
                "employee": responce,
            }
            return render(request, "workers_table/employee.html", context)
    return redirect('logout')
    
# API сотрудников компании
class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.DjangoFilterBackend]
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        Token.objects.create(user=self)
        serializer.save()

# API всех дней
class ControlViewSet(ModelViewSet):
    queryset = Control.objects.all()
    serializer_class = ControlSerializer
    filter_backends = [filters.DjangoFilterBackend]
    permission_classes = [IsAdminUser, ControlPermission]

# API присутствующих и убывших сотрудников и их время в нынешний день
class ControlThatDayViewSet(ModelViewSet):
    # сотрудники которые покинули в этот день рабочее место
    queryset_left = Control.objects\
        .filter(date=datetime.date.today(), status="LEFT")
    # сотрудники, которые находятся на рабочем месте
    queryset_arrived = Control.objects\
        .filter(date=datetime.date.today(), status="ARRIVED")\
        .exclude(employee__in=queryset_left.values_list("employee"))
    queryset = queryset_left.union(queryset_arrived)
    serializer_class = ControlSerializer
    filter_backends = [filters.DjangoFilterBackend]
    permission_classes = [IsAuthenticated]

# функции, которая отправляет регистрацию прибытия/убытие сотрудника
def post_control(request):
    if request.user.is_authenticated:
        # token = Token.objects.get(user=request.user)

        # проверка был ли у сотрудника этот статус сегодня
        status_repeat = 0
        status_repeat = Control.objects.filter(employee_id=request.POST["employee_id"],
            status=request.POST["status"], date=datetime.date.today()).count()
        impossible_status = 1

        # проверка при отправке статуса ушел, был ли отправлен в этот день статут прибыл
        if request.POST["status"] == "LEFT":
            impossible_status = Control.objects.filter(employee_id=request.POST["employee_id"],
            status="ARRIVED", date=datetime.date.today()).count()
        print(impossible_status, status_repeat)
        if impossible_status != 0 and status_repeat == 0:
            employee = Control(employee_id=request.POST["employee_id"],
                status=request.POST["status"],reason=request.POST["reason"]).save()
            return redirect("list")
        else:  
            return HttpResponse('Вы не можете выбрать данный статус')
            

"""diploma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from workers_table.views import (
    ControlThatDayViewSet,
    ControlViewSet, 
    EmployeeViewSet, 
    employee_page, 
    logout,
    post_control, 
    user_login, 
    workers, 
    homepage
    )

router = DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employees')
router.register('controls', ControlViewSet, basename='controling')
router.register('today', ControlThatDayViewSet, basename='control')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("list/", workers, name='list'),
    path('homepage/', homepage, name='homepage'),
    path('api/', include(router.urls)),
    path('', user_login, name='login'),
    path('logout/', logout, name='logout'),
    path('employee/', employee_page, name='get_employee'),
    path('post_control/', post_control, name='post_control'), 

]

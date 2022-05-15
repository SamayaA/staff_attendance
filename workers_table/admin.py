
from django.contrib import admin

from workers_table.models import Department, DepartmentHead, Employee, Position, Control, Vacation, Exceptions

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "first_name", "last_name", "phone", "department", "position")

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone")

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

@admin.register(DepartmentHead)
class DepartmentHeadAdmin(admin.ModelAdmin):
    list_display = ("id", "head", "department")

@admin.register(Control)
class ControlAdmin(admin.ModelAdmin):
    list_display = ("id", "employee", "date", "time", "status", "reason")

@admin.register(Vacation)
class VacationAdmin(admin.ModelAdmin):
    list_display = ("id", "employee", "start_date", "end_date")

@admin.register(Exceptions)
class ExceptionsAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "name")    
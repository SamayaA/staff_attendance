
from django.contrib import admin

from workers_table.models import Department, DepartmentHead, Employee, Position, Control

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [all]

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [all]

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = [all]

@admin.register(DepartmentHead)
class DepartmentHeadAdmin(admin.ModelAdmin):
    list_display = [all]

@admin.register(Control)
class ControlAdmin(admin.ModelAdmin):
    list_display = [all]
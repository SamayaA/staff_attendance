
from django.contrib import admin

from workers_table.models import Department, DepartmentHead, Employee, Position, Control, Vacation, Exceptions

# модель сотрудник
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "first_name", "last_name", "phone", "department", "position")

# модель отдел
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone")

# модель должность
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

# модель начальник отдела
@admin.register(DepartmentHead)
class DepartmentHeadAdmin(admin.ModelAdmin):
    list_display = ("id", "head", "department")

# модель контроль
@admin.register(Control)
class ControlAdmin(admin.ModelAdmin):
    list_display = ("id", "employee", "date", "time", "status", "reason")

# модель отпуск
@admin.register(Vacation)
class VacationAdmin(admin.ModelAdmin):
    list_display = ("id", "employee", "start_date", "end_date")

# модель исключения
@admin.register(Exceptions)
class ExceptionsAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "name")    
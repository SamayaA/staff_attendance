
from rest_framework import serializers

from workers_table.models import Control, Department, DepartmentHead, Employee, Exceptions, Vacation

class EmployeeSerializer(serializers.ModelSerializer):
    '''
    Employee
    args: username: CharField(), phone: PhoneNumberField(),
    email, password, 
    department: Department ID, position: Position ID,
    '''
    department = serializers.ReadOnlyField(source="department.name")
    position = serializers.ReadOnlyField(source="position.name")
    class Meta:
        model = Employee
        fields = ("id", "first_name", "last_name", "email", "phone", "department", "position")

class DepartmentHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentHead
        fields = ("department", "position")

class ControlSerializer(serializers.ModelSerializer):
    employee_first_name = serializers.ReadOnlyField(source="employee.first_name")
    employee_last_name = serializers.ReadOnlyField(source="employee.last_name")
    employee_id = serializers.UUIDField()
    class Meta:
        model = Control
        fields = ("id", "employee_id", "employee_first_name", "employee_last_name", "date", "time", "status", "reason")

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class ExceptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exceptions
        fields = "__all__"

class VacationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = "__all__"


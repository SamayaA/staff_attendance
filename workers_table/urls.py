from rest_framework.routers import DefaultRouter

from workers_table.views import (
    ControlThatDayViewSet,
    ControlViewSet, 
    EmployeeViewSet
)

router = DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employees')
router.register('controls', ControlViewSet, basename='controling')
router.register('today', ControlThatDayViewSet, basename='control')

urlpatterns = router.urls
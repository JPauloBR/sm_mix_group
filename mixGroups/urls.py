from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', views.EmployeeListView.as_view(), name='employees'),
    path('employee/<int:pk>', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('groups/', views.GroupListView.as_view(), name='groups'),
    path('group/<int:pk>', views.GroupDetailView.as_view(), name='group-detail'),
    path('employee/create/', views.EmployeeCreate.as_view(), name='employee_create'),
    path('employee/<int:pk>/update/', views.EmployeeUpdate.as_view(), name='employee_update'),
    path('employee/<int:pk>/delete/', views.EmployeeDelete.as_view(), name='employee_delete'),
    path('runprocess/', views.runprocess, name='runprocess'),

]
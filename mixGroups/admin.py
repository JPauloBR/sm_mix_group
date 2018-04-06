from django.contrib import admin
from .models import Employee, Group, History

# admin.site.register(Employee)
# admin.site.register(Group)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

admin.site.register(Employee, EmployeeAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_list', 'creation_date', 'expiration_date', 'runtime')

admin.site.register(Group, GroupAdmin)

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'runtime', 'creator')

admin.site.register(History, HistoryAdmin)



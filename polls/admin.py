from django.contrib.admin import site
from django.contrib.admin import ModelAdmin

from polls.models import Employee

class EmployeeAdmin(ModelAdmin):
 list_display = ['Name', 'Email', 'Department']


# Register your models here.


site.register(Employee,EmployeeAdmin)
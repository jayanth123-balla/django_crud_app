from django.contrib import admin 
from testapp.models import Company,Employee
 
# Register your models here. 
class CompanyAdmin(admin.ModelAdmin): 
    list_display=['name','location','ceo'] 
 
admin.site.register(Company,CompanyAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','name','salary','company']

admin.site.register(Employee,EmployeeAdmin)
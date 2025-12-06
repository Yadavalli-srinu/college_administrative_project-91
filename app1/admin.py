from django.contrib import admin

from app1.models import department_model,hod_model,professor_model,student_model

class department_admin(admin.ModelAdmin):
    list_display=["Department","Code"]
admin.site.register(department_model,department_admin)

class hod_admin(admin.ModelAdmin):
    list_display=["Name","Department","Phone"]
admin.site.register(hod_model,hod_admin)

class professor_admin(admin.ModelAdmin):
    list_display=["Name","Phone","Department","Subject"]
admin.site.register(professor_model,professor_admin)

class student_admin(admin.ModelAdmin):
    list_display=["Name","Register_id","Department","HOD"]
admin.site.register(student_model,student_admin)

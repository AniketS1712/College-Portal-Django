from django.contrib import admin
from academy.models import Students,faculty

class StudentAdmin(admin.ModelAdmin):
    list_display = ("Enrollment_no", "S_Name", "S_Age", "Course", "College",)
class  facultyAdmin(admin.ModelAdmin):
    list_display = ("F_Name","F_Designation","Subject","Department","Educational_Qualification",
    "Email","Specialization","Field_of_Interest","Teaching_Experience")
admin.site.register(Students, StudentAdmin)
admin.site.register(faculty, facultyAdmin)

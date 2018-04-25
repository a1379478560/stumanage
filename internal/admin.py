from django.contrib import admin

# Register your models here.
from internal import models
# Register your models here.

class stuAdmin(admin.ModelAdmin):
    list_display = ('name','parent_phone','qq','stu_id','status','school','class_id',)

admin.site.register(models.StuInfo,stuAdmin)
admin.site.register(models.ClassList)
admin.site.register(models.Course)

class teacherAdmin(admin.ModelAdmin):
    list_display = ('name','sex','phone','qq','entry_date','status','notice',)
admin.site.register(models.TeacherInfo,teacherAdmin)
admin.site.register(models.MarketerInfo)
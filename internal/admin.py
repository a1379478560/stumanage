from django.contrib import admin

# Register your models here.
from internal import models
# Register your models here.


@admin.register(models.StuInfo)
class stuAdmin(admin.ModelAdmin):
    list_display = ('name','sex','parent_phone','qq','stu_id','status','school','class_id',)
    list_per_page = 50
    list_display_links = ('qq', 'school')


@admin.register(models.TeacherInfo)
class teacherAdmin(admin.ModelAdmin):
    list_display = ('name','sex','phone','qq','entry_date','status','notice',)
    list_per_page = 50
    ordering = ('-entry_date',)
    list_filter = ('status', 'entry_date') #过滤器
    search_fields = ('name', )          #搜索字段
    date_hierarchy = 'entry_date'        #详细时间分层筛选
@admin.register(models.ClassList)
class classListAdmin(admin.ModelAdmin):
    list_display = ('name','course','course_type','is_online','class_hour','capacity','semester','start_date','graduate_date','teacher','notice')


@admin.register(models.MarketerInfo)
class marketAdmin(admin.ModelAdmin):
    list_display = ('name','sex','phone','qq','entry_date','status')


@admin.register(models.Course)
class courseAdmin(admin.ModelAdmin):
    list_display = ('name','suit_age','brief','notice')

@admin.register(models.SchoolInfo)
class schoolAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone','notice')


from django.contrib import admin
# from django.utils.translation import ugettext_lazy
from internal import models

# Register your models here.

# class MyAdminSite(admin.AdminSite):
#     site_header = 'icoding编程学院'


@admin.register(models.StuInfo)
class stuAdmin(admin.ModelAdmin):
    list_display = ('name','sex','parent_phone','qq','stu_id','status','school','class_id','notice',)
    list_per_page = 50
#    list_display_links = ('qq', 'school')
    list_editable = ('notice',)


@admin.register(models.TeacherInfo)
class teacherAdmin(admin.ModelAdmin):
    list_display = ('name','sex','phone','qq','join_date','status','notice',)
    list_editable = ('notice',)
    list_per_page = 50
    ordering = ('-join_date',)
    list_filter = ('status', 'join_date') #过滤器
    search_fields = ('name', )          #搜索字段
    date_hierarchy = 'join_date'        #详细时间分层筛选
@admin.register(models.ClassList)
class classListAdmin(admin.ModelAdmin):
    list_display = ('name','course','course_type','is_online','class_hour','capacity','semester','start_date','graduate_date','teacher','notice')
    list_editable = ('notice',)

@admin.register(models.MarketerInfo)
class marketAdmin(admin.ModelAdmin):
    list_display = ('name','sex','phone','qq','join_date','status','notice')
    list_editable = ('notice',)

@admin.register(models.Course)
class courseAdmin(admin.ModelAdmin):
    list_display = ('name','suit_age','brief','notice')
    list_editable = ('notice',)

@admin.register(models.SchoolInfo)
class schoolAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone','notice')
    list_editable = ('notice',)





# class MyAdminSite(admin.AdminSite):         #设置站点信息
#     # Text to put at the end of each page's <title>.
#     site_title = ugettext_lazy('iCODING编程学院')
#     # Text to put in each page's <h1> (and above login form).
#     site_header = ugettext_lazy('iCODING编程学院')
#     # Text to put at the top of the admin index page.
#     index_title = ugettext_lazy('iCODING编程学院')
# admin_site = MyAdminSite()
admin.site.site_header = 'ICODING编程学院'
admin.site.site_title='ICODING编程学院信息管理系统'
admin.site.index_title='ICODING编程学院'
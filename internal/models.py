from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#课程信息
class Course(models.Model):
    suit_age_choice = (
        ("elementary", "小学"),
        ("middle", "初中"),
        ("high", "高中"),
        ('college','大学'),
    )
    #course_id=models.IntegerField(unique=True)
    name=models.CharField(max_length=128)
    suit_age=models.CharField(choices=suit_age_choice,max_length=16,default='elementary')
    #price=models.IntegerField(default=0)
    #online_price=models.IntegerField(default=0)
    notice=models.TextField(blank=True)
    def __str__(self):
        return self.name

#班次信息
class ClassList(models.Model):
    name=models.CharField(max_length=16)
    is_online_choice=(
        ('online','在线上课'),
        ('offline','线下上课'),
    )
    course_type_choice=(
        ('in_school','校内上课'),
        ('full_time','全日制'),
        ('part_tim','非全日制')
    )
    #id=models.CharField(default='00',max_length=8)
#    course=models.ForeignKey('Course',on_delete=)
    course_type=models.CharField(choices=course_type_choice,default='in_school',max_length=32)
    is_online=models.CharField(choices=is_online_choice,default='offline',max_length=32)
    class_hour=models.IntegerField(default=50)
    capacity=models.IntegerField(default=30)
    semester=models.IntegerField(default=2)
    start_date=models.DateField()
    graduate_date=models.DateField(blank=True,null=True)
    teachers=models.ForeignKey('TeacherInfo',on_delete=models.PROTECT)
    notice=models.TextField(max_length=512,blank=True)
    def __str__(self):
       return "%s(%s)" %(self.name,self.course_type)


#学生信息
class StuInfo(models.Model):
    name=models.CharField(max_length=32,blank=True)
    sex_choice = (
        ('male', '男'),
        ('female', '女'),
    )
    sex = models.CharField(choices=sex_choice, max_length=8,default='male')
    qq = models.CharField(max_length=64, unique=True,null=True)
    parent_phone=models.CharField(blank=True,max_length=11)
    stu_id=models.CharField(blank=True,max_length=128,default='0000000000')
    school=models.CharField(blank=True,null=True,max_length=128)
    source_type=(('qq',u'qq群'),
                 ('school',u'学校转化'),
                 ('ads',u'广告'),
                 ('agent',u'招生代理'),
                 ('others',u'其他'),
                 )
    source=models.CharField(choices=source_type,default='agent',max_length=32)

    referee=models.ForeignKey('MarketerInfo',on_delete=models.SET_NULL,null=True,default=None)
    class_id=models.ForeignKey('ClassList',on_delete=models.SET_NULL,null=True)
    customer_note=models.TextField()
    status_choices=(
                ('signed',u'已报名'),
                 ('unregistered',u'未报名'),
                 ('graduated',u'已毕业'),
    )
    status=models.CharField(choices=status_choices,max_length=64)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s(%s)" %(self.qq,self.name)

#教师信息
class TeacherInfo(models.Model):
    name=models.CharField(max_length=32,blank=False)
    sex_choice=(
        ('male','男'),
        ('female','女'),
    )
    #id=models.CharField(default='000000',blank=False,null=False)
    sex=models.CharField(choices=sex_choice,max_length=8,default='male')
    qq = models.CharField(max_length=64, unique=True)
    phone=models.CharField(blank=True,max_length=11)
    notice=models.TextField(max_length=512,blank=True)
    entry_date=models.DateField(auto_now_add=True)
    status_choice=(
        ('signed','在职'),
        ('resigned','离职'),
    )
    status=models.CharField(choices=status_choice,default='signed',max_length=32)
    def __str__(self):
        return "%s(%s)" %(self.name,self.status)

#市场人员信息
class MarketerInfo(models.Model):
    name=models.CharField(max_length=32,blank=False)
    sex_choice=(
        ('male','男'),
        ('female','女'),
    )
    #id=models.CharField(default='000000',blank=False,null=False)
    sex=models.CharField(choices=sex_choice,max_length=8,default='male')
    qq = models.CharField(max_length=11, unique=True,blank=True)
    phone=models.CharField(blank=True,max_length=11)
    notice=models.TextField(blank=True,max_length=512)
    entry_date=models.DateField(auto_now_add=True)
    status_choice=(
        ('signed','在职'),
        ('resigned','离职'),
    )
    status=models.CharField(choices=status_choice,default='signed',max_length=32)
    def __str__(self):
        return "%s(%s)" %(self.name,self.status)






class SchoolInfo(models.Model):
    name=models.CharField(max_length=32)
    address=models.CharField(max_length=64,blank=True)
    phone=models.CharField(max_length=11,blank=True)
    notice=models.TextField(max_length=512,blank=True)


# def getReferee():
#     r = [('none', '----')]
#     for obj in MarketerInfo.objects.get().all():
#         r=r+[(obj.id, obj.name)]
#     return r
from django.db import models
from django.contrib.auth.models import User
from .fields import IdField
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
    name=models.CharField(max_length=128,verbose_name='课程')
    suit_age=models.CharField(choices=suit_age_choice,max_length=16,default='elementary',verbose_name='适用阶段')
    #price=models.IntegerField(default=0)
    #online_price=models.IntegerField(default=0)
    brief = models.TextField(blank=True, verbose_name='简介')
    notice=models.CharField(max_length=128,blank=True,verbose_name='备注')
    def __str__(self):
        return  self.name
    class Meta:
        verbose_name = '课程介绍'
        verbose_name_plural = verbose_name





#班次信息
class ClassList(models.Model):
    name=models.CharField(max_length=16,verbose_name='班次')
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
    course=models.ForeignKey('Course',on_delete=models.DO_NOTHING,verbose_name='科目')
    course_type=models.CharField(choices=course_type_choice,default='in_school',max_length=32,verbose_name='课程类型')
    is_online=models.CharField(choices=is_online_choice,default='offline',max_length=32,verbose_name='上课方式')
    class_hour=models.IntegerField(default=50,verbose_name='课时')
    capacity=models.IntegerField(default=30,verbose_name='最大班容量')
    semester=models.IntegerField(default=2,verbose_name='学期数')
    start_date=models.DateField(verbose_name='开班日期')
    graduate_date=models.DateField(blank=True,null=True,verbose_name='毕业日期')
    teacher=models.ForeignKey('TeacherInfo',on_delete=models.PROTECT,verbose_name='任课老师')
    notice=models.CharField(max_length=128,blank=True,verbose_name='备注')
    def __str__(self):
       return "%s(%s)" %(self.name,self.course_type)
    class Meta:
        verbose_name = '开班列表'
        verbose_name_plural = verbose_name




#学生信息
class StuInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=True)  # 创建该数据的登录用户
    name=models.CharField(max_length=32,blank=True,verbose_name = '姓名')
    sex_choice = (
        ('male', '男'),
        ('female', '女'),
    )
    sex = models.CharField(choices=sex_choice, max_length=8,default='male',verbose_name=' 性别')
    qq = models.CharField(max_length=64, unique=True,null=True,verbose_name = 'QQ')
    parent_phone=models.CharField(blank=True,max_length=11,verbose_name = '父母电话')
    stu_id=IdField(max_length=6,default='000000',verbose_name = '学号')
    school=models.CharField(blank=True,null=True,max_length=128,verbose_name = '学校')
    source_type=(('qq',u'qq群'),
                 ('school',u'学校转化'),
                 ('ads',u'广告'),
                 ('agent',u'招生代理'),
                 ('others',u'其他'),
                 )
    source=models.CharField(choices=source_type,default='agent',max_length=32,verbose_name = '来源')

    referee=models.ForeignKey('MarketerInfo',on_delete=models.SET_NULL,null=True,default=None,verbose_name = '招生人')
    class_id=models.ForeignKey('ClassList',on_delete=models.SET_NULL,null=True,verbose_name = '班次')
    notice=models.CharField(max_length=128,blank=True,verbose_name = '备注')
    status_choices=(
                ('signed',u'已报名'),
                 ('unregistered',u'未报名'),
                 ('graduated',u'已毕业'),
    )
    status=models.CharField(choices=status_choices,max_length=64,verbose_name = '状态')
    join_date=models.DateField(verbose_name = '入学日期')

    def __str__(self):
        return "%s" %(self.name)
    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = '学生信息'




#教师信息
class TeacherInfo(models.Model):
    user = models.OneToOneField(User, verbose_name='用户名', on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=32,blank=False,verbose_name = '姓名')
    sex_choice=(
        ('male','男'),
        ('female','女'),
    )
    #id=models.CharField(default='000000',blank=False,null=False)
    sex=models.CharField(choices=sex_choice,max_length=8,default='male',verbose_name = '性别')
    qq = models.CharField(max_length=64, unique=True,verbose_name = 'QQ')
    phone=models.CharField(blank=True,max_length=11,verbose_name = '电话')
    notice=models.CharField(max_length=128,blank=True,verbose_name = '备注')
    join_date=models.DateField(auto_now_add=True,verbose_name = '入职时间')
    status_choice=(
        ('signed','在职'),
        ('resigned','离职'),
    )
    status=models.CharField(choices=status_choice,default='signed',max_length=32,verbose_name = '状态')
    def __str__(self):
        return "%s(%s)" %(self.name,self.status)
    class Meta:
        verbose_name = '教师信息'
        verbose_name_plural = '教师信息'




#市场人员信息
class MarketerInfo(models.Model):
    user=models.OneToOneField(User,verbose_name='用户名',on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=32,blank=False,verbose_name = '姓名')
    sex_choice=(
        ('male','男'),
        ('female','女'),
    )
    sex=models.CharField(choices=sex_choice,max_length=8,default='male',verbose_name = '性别')
    qq = models.CharField(max_length=11, unique=True,blank=True,verbose_name = 'QQ')
    phone=models.CharField(blank=True,max_length=11,verbose_name = '电话')
    notice=models.CharField(blank=True,max_length=128,verbose_name = '备注')
    join_date=models.DateField(verbose_name = '入职时间')
    status_choice=(
        ('signed','在职'),
        ('resigned','离职'),
    )
    status=models.CharField(choices=status_choice,default='signed',max_length=32,verbose_name = '状态')
    def __str__(self):
        return "%s(%s)" %(self.name,self.status)
    class Meta:
        verbose_name = '市场人员'
        verbose_name_plural = '市场人员'


#学校信息
class SchoolInfo(models.Model):
    name=models.CharField(max_length=32,verbose_name='学校名')
    address=models.CharField(max_length=64,blank=True,verbose_name='地址')
    phone=models.CharField(max_length=11,blank=True,verbose_name='电话')
    notice=models.CharField(max_length=128,blank=True,verbose_name='备注')
    def __str__(self):
        return "%s" %(self.name)
    class Meta:
        verbose_name = '学校列表'
        verbose_name_plural = verbose_name


#上课记录
class ClassRecord(models.Model):
    start_time=models.DateTimeField(verbose_name='上课时间')
    address=models.CharField(max_length=128,verbose_name='上课地点',default='海悦天地')
    class_id=models.ForeignKey('ClassList',on_delete=models.DO_NOTHING,verbose_name='班次')
    which_time=models.IntegerField(default=1,verbose_name='第几次课')
    teacher=models.ForeignKey('TeacherInfo',on_delete=models.DO_NOTHING,verbose_name='上课老师')
    duration=models.IntegerField(default=2,verbose_name='上课学时')
    should_come_num=models.IntegerField(verbose_name='应到人数')
    absentee=models.CharField(blank=True,max_length=128,verbose_name='缺席名单')
    notice=models.CharField(max_length=128,blank=True,verbose_name='备注')
    def __str__(self):
        return "%s上课记录" %self.class_id
    class Meta:
        verbose_name='上课记录'
        verbose_name_plural=verbose_name
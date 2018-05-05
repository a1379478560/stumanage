from django.shortcuts import render
from . import models
from django.http import  HttpResponse
from  stumanage.settings import BASE_DIR
from . import forms
import time,datetime
import xlrd
from django.db import transaction
# Create your views here.
def upload(request):
    if not request.user.is_superuser:
        return HttpResponse('只有超级管理员有权限')
    if request.method == 'GET':
        form_obj = forms.uploadRecordForm()
        return render(request,'upload.html',{'obj':form_obj})
    elif request.method=="POST":
        form_obj=forms.uploadRecordForm(request.POST,request.FILES)
        # handle_xls(request.FILES['file'].read())
        try:
            flag=handle_xls(request.FILES['file'].read())   #返回三个值，第一个是出错的行，全部正确则为0。第二个是一共（或者出错前）成功创建的记录数，第三个是数据正确但是重复的条数
        except xlrd.XLRDError:
            return HttpResponse('文件格式有错误！<br><br><br><a href="upload">继续上传</a>')
        # except IntegrityError :
        #     return HttpResponse('数据有重复！')
        # except :
        #     return HttpResponse('未知错误！')
        if flag[0]>0:
            return HttpResponse('第%s行数据格式不正确，请检查！ 已创建%s条记录，略过%s条重复记录。<br><br><br><a href="upload">继续上传</a>' %(flag[0],flag[1],flag[2]))
        if form_obj.is_valid():
            form_obj.created = flag[1]
            form_obj.duplicated = flag[2]
            form_obj.notice='???'
            form_obj.save()
        return HttpResponse('上传成功！ 创建%s条记录，略过%s条重复记录<br><br><br><a href="upload">继续上传</a>' %(flag[1],flag[2]))

#@transaction.set_autocommit(False)
def handle_xls(xlsc_ontent):      # 处理Excel表格
    all_created=0
    duplicated=0
    stus=[]
    wb=xlrd.open_workbook(filename=None,file_contents=xlsc_ontent)
    sheet1=wb.sheet_by_index(0)
    for raw in range(1,sheet1.nrows):
        print(type(sheet1.cell(raw,1).value))
        try:
            if sheet1.cell(raw,1).value=='男':
                sex='male'
            else:
                sex='female'
            print(sex)
            referee=models.MarketerInfo.objects.get(name=sheet1.cell(raw,6).value)
            print(referee)
            class_list=models.ClassList.objects.get(name=str(sheet1.cell(raw,8).value))

            choice={'已报名':'signed','未报名':'unregistered','已毕业':'graduated'}
            status=choice[sheet1.cell(raw,5).value]
            print(status)
            if sheet1.cell(raw, 7).value=='空':
                school=''
            else:
                school=sheet1.cell(raw,7).value
        except :
            return raw,all_created,duplicated
        try:
            stu,created=models.StuInfo.objects.update_or_create(
                name=sheet1.cell(raw,0).value,
                parent_phone=str(my_int(sheet1.cell(raw,2).value)),
                qq=str(my_int(sheet1.cell(raw,3).value)),
                stu_id=str(my_int(sheet1.cell(raw,4).value)),
                notice=sheet1.cell(raw,9).value,
                user_id=referee.user_id,
                school=school,
                sex = sex,
                status=status,
                referee=referee,
                class_id=class_list,
                join_date=datetime.date.today()
            )
        except ValueError:
            #raise
            return raw+1,all_created,duplicated
        if created :
            all_created+=1
        else:
            duplicated+=1
    return  0,all_created,duplicated
def my_int(num):
    if num=="":
        return 0
    else:
        return int(num)
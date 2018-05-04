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
        print(form_obj.is_valid())
        print(form_obj.cleaned_data)
        print(form_obj.errors)
        # handle_xls(request.FILES['file'].read())
        try:
            flag=handle_xls(request.FILES['file'].read())
        except xlrd.XLRDError:
            return HttpResponse('文件格式有错误！')
        # except IntegrityError :
        #     return HttpResponse('数据有重复！')
        # except :
        #     return HttpResponse('未知错误！')
        if flag>0:
            return HttpResponse('第%s行数据格式不正确，请检查！' % flag)
        if form_obj.is_valid():
            form_obj.save()
        return HttpResponse('ok')

#@transaction.set_autocommit(False)
def handle_xls(xlsc_ontent):      # 处理Excel表格
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
            return raw
        stu,created=models.StuInfo.objects.update_or_create(
            name=sheet1.cell(raw,0).value,
            parent_phone=str(int(sheet1.cell(raw,2).value)),
            qq=str(int(sheet1.cell(raw,3).value)),
            stu_id=str(int(sheet1.cell(raw,4).value)),
            notice=sheet1.cell(raw,9).value,
            school=school,
            sex = sex,
            status=status,
            referee=referee,
            class_id=class_list,
            join_date=datetime.date.today()
        )
        print(created)
        # stu.save()
        # stus.append(stu)
        # with transaction.atomic():
        #     for stu in stus:
        #         stu.save()
    return  0
from django.shortcuts import render
from django.http import  HttpResponse
from  stumanage.settings import BASE_DIR
from . import forms
import xlrd
# Create your views here.
def upload(request):
    if request.method == 'GET':
        form_obj = forms.uploadRecordForm()
        return render(request,'upload.html',{'obj':form_obj})
    elif request.method=="POST":
        form_obj=forms.uploadRecordForm(request.POST,request.FILES)
        print(form_obj.is_valid())
        print(form_obj.cleaned_data)
        print(form_obj.errors)
        handle_xls(request.FILES['file'].value())
        if form_obj.is_valid():
            print('okok')
            form_obj.save()
        return HttpResponse('ok')
def handle_xls(file):
    wb=xlrd.open_workbook(file)
    sheet1=wb.sheet_by_index(0)
    print(sheet1.ncols)
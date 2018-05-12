import xlrd
from . import models
from django.db import IntegrityError
import time,datetime


# 导入某一个不合规范的excel表格而专门写的处理函数
def handle_xls_5_9(xlsc_ontent):      # 处理Excel表格
    all_created=0
    duplicated=0
    xiao=0
    wb=xlrd.open_workbook(filename=None,file_contents=xlsc_ontent)
    for i in range(1):
        sheet1=wb.sheet_by_index(i)
        for raw in range(1,sheet1.nrows):
            # print(type(sheet1.cell(raw,1).value))
            try:
                sex_key={
                    '男':'male',
                    '女':'female',
                }
                sex=sex_key[sheet1.cell(raw,1).value]
                status='unregistered'
                school=models.SchoolInfo.objects.get(name='维明路小学')
                grade=6


                try:
                    str_tel1=str(sheet1.cell(raw, 2).value)
                    str_tel2 = str(sheet1.cell(raw, 3).value)
                    if len(str_tel1)<11:
                        str_tel1=''
                    if len(str_tel2)<11:
                        str_tel2=''
                    if len(str_tel1) < 11 and len(str_tel2)<11 :
                        print(str_tel1)
                        xiao+=1

                        continue
                    elif len(str_tel1)>11 or len(str_tel2)>11 :
                        str_tel1=str_tel1[:11]
                        str_tel2 = str_tel2[:11]
                except:
                    raise
                    duplicated+=1
                    continue
                if str_tel2=='' :
                    parent_phone=str_tel1
                elif str_tel1=='':
                    parent_phone=str_tel2
                else:
                    parent_phone=str_tel1+'&'+str_tel2
            except :
                raise
                #return raw,all_created,duplicated
            try:
                stu,created=models.StuInfo.objects.update_or_create(
                    name=sheet1.cell(raw,0).value,
                    parent_phone=parent_phone,
                    grade=grade,
                    is_paid=False,
                    school=school,
                    sex = sex,
                    status=status,

                    join_date='2017-3-1'
                )
            except ValueError:
                raise
                #return raw+1,all_created,duplicated
            except IntegrityError:
                duplicated+=1
                continue
            if created :
                all_created+=1
            else:
                duplicated+=1
    print(xiao)
    return  0,all_created,duplicated
def my_int(num):
    if num=="":
        return 0
    else:
        return int(num)

    # # 导入某一个不合规范的excel表格而专门写的处理函数
    # def handle_xls_5_9(xlsc_ontent):  # 处理Excel表格
    #     all_created = 0
    #     duplicated = 0
    #     stus = []
    #     wb = xlrd.open_workbook(filename=None, file_contents=xlsc_ontent)
    #     sheet1 = wb.sheet_by_index(0)
    #     for raw in range(1, sheet1.nrows):
    #         print(type(sheet1.cell(raw, 1).value))
    #         try:
    #             sex = 'unknown'
    #
    #             status = 'unregistered'
    #             school = models.SchoolInfo.objects.get(name='东风小学')
    #             grade_chinese = sheet1.cell(raw, 2).value[0]
    #             key = {
    #                 '一': 1,
    #                 '二': 2,
    #                 '三': 3,
    #                 '四': 4,
    #                 '五': 5,
    #                 '六': 6,
    #             }
    #             grade = key[grade_chinese]
    #         except:
    #             return raw, all_created, duplicated
    #         try:
    #             stu, created = models.StuInfo.objects.update_or_create(
    #                 name=sheet1.cell(raw, 1).value,
    #                 parent_phone=str(my_int(sheet1.cell(raw, 3).value)),
    #                 grade=grade,
    #                 is_paid=False,
    #
    #                 school=school,
    #                 sex=sex,
    #                 status=status,
    #
    #                 join_date='2017-3-30'
    #             )
    #         except ValueError:
    #             # raise
    #             return raw + 1, all_created, duplicated
    #         except IntegrityError:
    #             duplicated += 1
    #             continue
    #         if created:
    #             all_created += 1
    #         else:
    #             duplicated += 1
    #     return 0, all_created, duplicated


# # 导入某一个不合规范的excel表格而专门写的处理函数
# def handle_xls_5_9(xlsc_ontent):      # 处理Excel表格
#     all_created=0
#     duplicated=0
#     xiao=0
#     stus=[]
#     wb=xlrd.open_workbook(filename=None,file_contents=xlsc_ontent)
#     for i in range(7):
#         sheet1=wb.sheet_by_index(i)
#         for raw in range(1,sheet1.nrows):
#             # print(type(sheet1.cell(raw,1).value))
#             try:
#                 sex='unknown'
#                 status='unregistered'
#                 school=models.SchoolInfo.objects.get(name='友谊大街小学')
#                 grade=3
#                 if not sheet1.cell(raw,2).value:
#                     notice=''
#                 else:
#                     notice=sheet1.cell(raw,2).value
#
#                 try:
#                     str_tel=str(sheet1.cell(raw, 1).value)
#                     if len(str_tel) < 11 :
#                         print(str_tel)
#                         xiao+=1
#                         duplicated+=1
#                         continue
#                     elif len(str_tel)>11 :
#                         str_tel=str_tel[:11]
#                 except:
#                     raise
#                     duplicated+=1
#                     continue
#
#                 parent_phone=str_tel
#             except :
#                 #raise
#                 return raw,all_created,duplicated
#             try:
#                 stu,created=models.StuInfo.objects.update_or_create(
#                     name=sheet1.cell(raw,0).value,
#                     parent_phone=parent_phone,
#                     grade=grade,
#                     is_paid=False,
#                     school=school,
#                     sex = sex,
#                     status=status,
#                     notice=notice,
#                     join_date='2017-5-10'
#                 )
#             except ValueError:
#                 #raise
#                 return raw+1,all_created,duplicated
#             except IntegrityError:
#                 duplicated+=1
#                 continue
#             if created :
#                 all_created+=1
#             else:
#                 duplicated+=1
#     print(xiao)
#     return  0,all_created,duplicated

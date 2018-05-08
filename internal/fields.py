from django.db import models
import ast
# 自定义IdField，用来存储学号
class IdField(models.CharField):
    description = "a custom class to story students id"

    # 继承CharField
    def __init__(self, *args, **kwargs):
        super(IdField, self).__init__(*args, **kwargs)
    # 读取数据库的时候调用这个方法
    def from_db_value(self, value, expression, conn, context):
        if not value:
            value = None
        return  value

    # 保存数据库的时候调用这个方法
    def get_prep_value(self, value):
        if value==None:
            return value
        if len(value)<6:
            return  value.zfill(6)
        return value

#自定义ListField，用来存储缺席的人,继承于TextField这个类
class ListFiled(models.TextField):         #暂时不用了
    description = "a listfiled"

    # 继承TextField
    def __init__(self, *args, **kwargs):
        super(ListFiled, self).__init__(*args, **kwargs)
    def from_db_value(self, value, expression, conn, context):
        if not value:
            value = []
        if isinstance(value, list):
            items=''
            for i in value:
                items+=i+' '
            return items
        # 直接将字符串转换成python内置的list
        return ast.literal_eval(value)

    # 保存数据库的时候调用这个方法
    def get_prep_value(self, value):
        if not value:
            return value
        return str(value)
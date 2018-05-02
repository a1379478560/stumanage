from django.apps import AppConfig

from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem  # 这两行是suit的配置

# class InternalConfig(AppConfig):
#     name = 'internal'
#     verbose_name='信息管理系统'



class SuitConfig(DjangoSuitConfig):    #suit
    layout = 'vertical'



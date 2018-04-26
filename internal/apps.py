from django.apps import AppConfig

from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem  # 这两行是suit的配置

class InternalConfig(AppConfig):
    name = 'internal'



class SuitConfig(DjangoSuitConfig):    #suit
    layout = 'vertical'



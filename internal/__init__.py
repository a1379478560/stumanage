#coding:utf8
from django.apps import AppConfig
import os

default_app_config='internal.InternalConfig'

def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]

class InternalConfig(AppConfig):
    name=get_current_app_name(__file__)
    #verbose_name='内部信息系统'
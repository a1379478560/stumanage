# Generated by Django 2.0.4 on 2018-05-05 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0009_auto_20180504_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadrecord',
            name='created',
            field=models.IntegerField(null=True, verbose_name='成功创建的记录数'),
        ),
        migrations.AddField(
            model_name='uploadrecord',
            name='duplicated',
            field=models.IntegerField(null=True, verbose_name='重复数据'),
        ),
    ]
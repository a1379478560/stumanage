# Generated by Django 2.0.4 on 2018-05-04 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0007_remove_uploadrecord_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuinfo',
            name='name',
            field=models.CharField(blank=True, max_length=16, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='stuinfo',
            name='parent_phone',
            field=models.CharField(blank=True, max_length=11, verbose_name='家长电话'),
        ),
        migrations.AlterField(
            model_name='uploadrecord',
            name='file',
            field=models.FileField(upload_to='internal/upload/', verbose_name='导入文件'),
        ),
    ]
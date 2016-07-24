# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_remove_taskmodel_task_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplTaskModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_task_content', models.CharField(max_length=256)),
                ('c_check_list', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='DoneTaskModel',
        ),
    ]
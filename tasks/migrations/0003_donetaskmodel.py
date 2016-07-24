# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_taskmodel_task_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoneTaskModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_content', models.CharField(default='YourDoneTask', max_length=1024)),
                ('check_list', models.BooleanField(default=False)),
            ],
        ),
    ]
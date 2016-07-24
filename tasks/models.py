from django.db import models

# Create your models here.


class TaskModel(models.Model):
    class Meta(object):
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    task_content = models.CharField(
        max_length=1024,
        blank=False,
        default='YourTask',
    )
    checkbox = models.BooleanField(
        default=False,
    )

    # new in Python3(it was __unicode__() in Python2)
    def __str__(self):
        return "%s" % self.task_content


class ComplTaskModel(models.Model):
    class Meta(object):
        verbose_name = "Completed Task"
        verbose_name_plural = "Completed Tasks"

    c_task_content = models.CharField(
        max_length=256,
        blank=False,
        default='ComplTask',
    )
    c_check_list = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return "%s" % self.c_task_content

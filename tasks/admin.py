from django.contrib import admin
from .models import TaskModel, ComplTaskModel
# Register your models here.

admin.site.register(TaskModel)
admin.site.register(ComplTaskModel)



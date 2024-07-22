from django.contrib import admin

from task_board.models import SubtaskItem, TaskItem

# Register your models here.
admin.site.register(TaskItem)
admin.site.register(SubtaskItem)
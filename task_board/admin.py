from django.contrib import admin

from task_board.models import ContactSgl, SubtaskItem, TaskItem

# Register your models here.
admin.site.register(TaskItem)
admin.site.register(SubtaskItem)
admin.site.register(ContactSgl)
from turtle import title
from django.db import models
from django.conf import settings
from datetime import date
from django.contrib.auth.models import User

class TaskItem(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=400)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    priority = models.CharField(max_length=50)
    task_board = models.CharField(max_length=50)
    created_at = models.DateField(default=date.today)
    due_date = models.DateField(default=date.today)
    task_id = models.IntegerField(unique=True)
    # category = models.CharField(max_length=50) 
    
    def __str__(self):
        # return str(self.id) + ' ' + self.title oder
        return f'({self.id}) {self.title}'

class SubtaskItem(models.Model):
    task = models.ForeignKey(
        TaskItem,
        related_name='subtasks',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=400)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f'({self.id}) {self.title}'
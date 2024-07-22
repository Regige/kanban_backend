from rest_framework import serializers
from .models import TaskItem

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TaskItem
        fields = '__all__'
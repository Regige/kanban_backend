from rest_framework import serializers
from .models import SubtaskItem, TaskItem

class SubtaskItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubtaskItem
        fields = ['id', 'title', 'completed']

class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskItemSerializer(many=True, required=False)
    class Meta:
        model = TaskItem
        fields = ['id', 'title', 'text', 'author', 'priority', 'task_board', 'created_at', 'due_date', 'task_id', 'subtasks']
        
    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        task = TaskItem.objects.create(**validated_data)
        for subtask_data in subtasks_data:
            SubtaskItem.objects.create(task=task, **subtask_data)
        return task
        
        
        
        
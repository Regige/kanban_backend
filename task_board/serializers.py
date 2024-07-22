from rest_framework import serializers
from .models import SubtaskItem, TaskItem

class SubtaskItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubtaskItem
        fields = ['id']


class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskItemSerializer(many=True, required=False)
    class Meta:
        model = TaskItem
        fields = '__all__'
        
    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        task = TaskItem.objects.create(**validated_data)
        if subtasks_data:  # Überprüfe, ob subtasks_data vorhanden ist
            for subtask_data in subtasks_data:
                SubtaskItem.objects.create(task=task, **subtask_data)
        return task
        
        
        
        
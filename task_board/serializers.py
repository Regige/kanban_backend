from rest_framework import serializers
from .models import ContactSgl, SubtaskItem, TaskItem


class ContactSglSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSgl
        # fields = ['id', 'title', 'email', 'phone', 'logogram', 'hex_color', 'author']
        fields = '__all__'
        

class SubtaskItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubtaskItem
        fields = ['id', 'task', 'title', 'completed']

class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskItemSerializer(many=True, required=False)
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=ContactSgl.objects.all(), many=True, required=False)

    class Meta:
        model = TaskItem
        fields = ['id', 'title', 'text', 'author', 'priority', 'task_board', 'created_at', 'due_date', 'subtasks', 'assigned_to', 'category']
        
    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        contacts_data = validated_data.pop('assigned_to', [])
        task = TaskItem.objects.create(**validated_data)
        for subtask_data in subtasks_data:
            SubtaskItem.objects.create(task=task, **subtask_data)
        task.assigned_to.set(contacts_data)
        return task
        
        
        
        
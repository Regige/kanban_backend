from rest_framework import serializers
from .models import ContactSgl, SubtaskItem, TaskItem
from django.contrib.auth.models import User


class ContactSglSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSgl
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
        fields = ['id', 'title', 'text', 'author', 'priority', 'task_board', 'created_at', 'due_date', 'assigned_to', 'category', 'subtasks']
        
    def create(self, validated_data):
        contacts_data = validated_data.pop('assigned_to', [])
        task = TaskItem.objects.create(**validated_data)
        task.assigned_to.set(contacts_data)
        return task
        
        
        
        
class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
            
        if password != password2:
            raise serializers.ValidationError({"Error": "Password does not match"})
            
        if User.objects.filter(email = self.validated_data['email']).exists():
            raise serializers.ValidationError({"Error": "Email already exist"})
            
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()
            
        return account
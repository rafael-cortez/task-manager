# serializers.py
from rest_framework import serializers
from .models import Board, TaskList, Task

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
# serializers.py
from rest_framework import serializers
from main.models import Task

class TaskSerializer(serializers.ModelSerializer):
    # serializers convert to work with api
    class Meta:
        model = Task
        fields = '__all__'

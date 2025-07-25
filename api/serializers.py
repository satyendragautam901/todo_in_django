# serializers.py
from rest_framework import serializers
from main.models import Task


# class TaskSerializer(serializers.ModelSerializer):
#     # serializers convert to work with api
#     class Meta:
#         model = Task
#         fields = '__all__'


# normal serializer
class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100) 
    description = serializers.CharField(allow_blank=True, required=False)  # This replaces TextField
    is_completed = serializers.BooleanField(default=False)

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

    
    

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data): # this will create an entry in db
        return Task.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        # instance is old data
        # validate_date is new data
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)

        instance.save()

        return instance
# class TaskViewSet(ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Task.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from main.models import Task
from .serializers import TaskSerializer

# @api_view(['GET'])
# def get_all_tasks(request):
#     tasks = Task.objects.all()
#     serializer = TaskSerializer(tasks, many=True) # many true because many items
#     return Response(serializer.data) # response is build in drf

def all_tasks(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many = True)

    return JsonResponse(serializer.data, safe=False) # this will convert to json data

def single_tasks(request,pk):

    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(task) # here no need to define many = true bcz single task

    return JsonResponse(serializer.data, safe=False) # this will convert to json data


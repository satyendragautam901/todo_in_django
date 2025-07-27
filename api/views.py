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
from .serializers import *
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# @api_view(['GET'])
# def get_all_tasks(request):
#     tasks = Task.objects.all()
#     serializer = TaskSerializer(tasks, many=True) # many true because many items
#     return Response(serializer.data) # response is build in drf

def all_tasks(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many = True) # python native data
    print("serializer data ", serializer.data)
    return JsonResponse(serializer.data, safe=False) # this will convert to json data

def single_tasks(request,pk):

    task = Task.objects.get(id = pk) # complex data because directly orm handles 
    serializer = TaskSerializer(task) # here no need to define many = true bcz single task

    return JsonResponse(serializer.data, safe=False) # this will convert to json data

@csrf_exempt
@api_view(['post'])
def create_task(request):
    if(request.method == "POST"):
        data = request.data # first fetch the data
        print("requested data ",data)

        # just for testing: assign any user (replace 1 with actual user id)
        user = User.objects.get(id=1)
        data['user'] = user.id  # include user ID in data

        serializer = TaskSerializer(data = data)

        if(serializer.is_valid()):
            serializer.save()
            
            return Response({ # if the task is create successfully
                "status": True,
                "data": serializer.data,
                "message": "Task created successfully"
            })
        
        return Response({ # if error during creating task.
                "status": False,
                "data": serializer.errors,
                "message": "Error during creating task"
            })


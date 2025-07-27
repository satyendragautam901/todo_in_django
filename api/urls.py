from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/', all_tasks, name='all_tasks'),
    path('tasks/<int:pk>', single_tasks),
    path('create-task/',create_task),
]

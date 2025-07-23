from django.urls import path
from .views import get_all_tasks

urlpatterns = [
    path('tasks/', get_all_tasks, name='get_all_tasks'),
]

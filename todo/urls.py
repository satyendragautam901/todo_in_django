"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view, name="home"),
    path('register/',register_view, name='register'),
    path('login/',login_view, name='login'),
    path('logout/',logout_view, name='logout'),

    # create todo
    path('create-todo/', create_todo, name='create_todo'),

    # update todo
    path('update-todo/<int:id>', update_todo, name='update_todo'),

    path('delete-todo/<int:id>/', delete_todo, name='delete_todo'),
    path('filter/<str:is_completed>/', filter_todo_view, name='filter_todo'),

    # ✅ DRF API route included here ONCE
    path('api/', include('api.urls')),
]

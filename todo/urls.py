"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from task.views import home, task, editTask, editTaskFull, addTask, deleteTask, searchTask, taskAll, stateTask, asingTask, asingTaskUser, asingTaskUserAsing
from apps.users.views import addUsers, users, editUser, deleteUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('task/', task, name="task"),
    path('task_all/', taskAll, name="taskAll"),
    path('edit_task/', editTask, name="editTask"),
    path('edit_task_full/', editTaskFull, name="editTaskFull"),
    path('add_task/', addTask, name="addTask"),
    path('delete_task/', deleteTask, name="deleteTask"),
    path('search_task/', searchTask, name="searchTask"),
    path('state_task/', stateTask, name="stateTask"),
    path('add_users/', addUsers, name="addUsers"),
    path('users/', users, name="users"),
    path('edit/', editUser, name="edit_user"),
    path('delete_user/', deleteUser, name="delete_user"),
    path('asing_task/', asingTask, name="asing_task"),
    path('asing_task_user/', asingTaskUser, name="asing_task_user"),
    path('asing_task_user_asing/', asingTaskUserAsing, name="asing_task_user_asing"),
]

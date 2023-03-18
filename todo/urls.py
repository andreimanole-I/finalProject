from django.urls import path

from todo import views

urlpatterns = [
    path('create_task/', views.TaskCreateView.as_view(), name='create-task'),
    path('task_list/', views.TaskListView.as_view(), name='task-list'),
]
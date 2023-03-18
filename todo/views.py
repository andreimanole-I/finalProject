from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from todo.forms import TaskForm
from todo.models import Task


class TaskCreateView(CreateView):
    template_name = 'todo/create_task.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task-list')


class TaskListView(ListView):
    template_name = "todo/task_list.html"
    model = Task
    context_object_name = "all_tasks"

    def get_queryset(self):
        return Task.objects.all()


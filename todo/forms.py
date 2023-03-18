from django import forms
from django.forms import TextInput, Select, DateInput, Textarea

from todo.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['task', 'description', 'assigned_to', 'deadline']

        widgets = {
            "task": TextInput(attrs={"placeholder": "Enter task name", "class": "form-control"}),
            "description": Textarea(attrs={'placeholder': 'Task description', 'class': 'form-control'}),
            'assigned_to': Select(attrs={'class': 'form-select'}),
            'deadline': DateInput(attrs={'class': 'form-control', 'type': 'date'}),

        }
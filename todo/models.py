from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):

    user_choices = [(user.username, user.username) for user in User.objects.all()]

    task = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    deadline = models.DateField()
    assigned_to = models.CharField(max_length=20, choices=user_choices)
    status = models.IntegerField(default=0)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.task

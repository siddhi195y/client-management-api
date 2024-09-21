
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, related_name='created_clients', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='assigned_projects')
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, related_name='created_projects', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

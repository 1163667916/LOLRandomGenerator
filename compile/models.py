from django.db import models
from django.utils import timezone

# Create your models here.


class Project(models.Model):
    name = models.CharField(default='', max_length=255)


class User(models.Model):
    name = models.CharField(default='', max_length=255)
    email = models.CharField(default='', max_length=100)


class Task(models.Model):
    branch = models.CharField(default='', max_length=255)
    job_name = models.CharField(default='', max_length=255)
    job_id = models.IntegerField(default=0)
    status = models.CharField(default='', max_length=10)
    variables = models.JSONField(default=dict)
    platform = models.CharField(default='', max_length=20)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True)
    command = models.CharField(default='', max_length=255)
    version = models.CharField(default='', max_length=30)
    project = models.ForeignKey(
        Project, on_delete=models.DO_NOTHING, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

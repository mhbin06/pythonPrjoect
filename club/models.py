from django.db import models
from django.contrib.auth.models import User

class Schedule(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

class Dashboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    progress = models.IntegerField()
    last_updated = models.DateField()

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

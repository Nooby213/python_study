from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=10)
    work = models.CharField(max_length=100)
    content = models.TextField()
    is_completed = models.BooleanField()
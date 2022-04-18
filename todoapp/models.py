from importlib.resources import contents
from importlib.resources import contents
from django.db import models

# Create your models here.
class TodoListItems(models.Model):
    content=models.TextField()
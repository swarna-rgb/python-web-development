from django.db import models

# Create your models here

class ToDoItem(models.Model):
    todoitem = models.TextField()

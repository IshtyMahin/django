from django.db import models
from category.models import Category
# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_Completed = models.BooleanField(default=False)
    TaskAssignDate = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category) 
    
    def __str__(self):
        return self.taskTitle
from django.db import models
from categories.models import Category
from authors.models import Author
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category) # ekta post er modye multiple category takte pare, ekta category multiple post er modye  takte pare.
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
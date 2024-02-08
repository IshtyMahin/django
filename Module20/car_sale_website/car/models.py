from django.db import models

from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100,unique=True,null=True, blank=True)

    def save(self, *args, **kwargs):
            if self.slug is None: 
                self.slug = slugify(self.name)  
            super().save(*args, **kwargs)
            
    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="car/media/uploads/", blank=True, null=True)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE,related_name="comments")
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"
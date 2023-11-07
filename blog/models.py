from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    pass

class Category(models.Model):
    nameCategory = models.CharField(max_length=15, blank=True)
    users = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='category')

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')

class Comment(models.Model):
    substance = models.TextField(null=True)
    users = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
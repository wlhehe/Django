from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True, max_length=20)
    password = models.CharField(max_length=15, unique=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    userName = models.CharField(max_length=15)

class Category(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_mow_add=True)

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')

class Comment(models.Model):
    substance = models.TextField(null=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
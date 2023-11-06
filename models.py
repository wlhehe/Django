from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    id = models.AutoField(primary_key=True, max_length=20)
    password = models.CharField(max_length=15, unique=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    userName = models.CharField(max_length=15)

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_mow_add=True)
    # class Meta:
    #     db_table = "post"

class Category(models.Model):
    nameCategory = models.CharField(max_length=15)
    # class Meta:
    #     db_table = "category"

class Comment(models.Model):
    substance = models.TextField(null=True)
    # class Meta:
    #     db_table = "comment"
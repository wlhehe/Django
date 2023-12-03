from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): # 회원가입, 로그인, 로그아웃
    pass

class Post(models.Model): # 게시물 리스트 조회, 게시물 하나만 조회, 게시물 수정, 게시물 삭제, 게시물 작성
    title = models.CharField(max_length=50)
    content = models.TextField(null=True)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

class Comment(models.Model):
    substance = models.TextField(null=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
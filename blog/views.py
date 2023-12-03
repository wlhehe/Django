from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import *
from django.contrib.auth import authenticate, login, logout

def home_view(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        User.objects.create_user(username=username, password=password).save()

        return redirect('login_view')

def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login_view')

def logout_view(request):
    logout(request)
    return redirect('home_view')


def post_create_view(request):
    if request.method == "GET":
        return render(request, 'post_create.html')
    elif request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        post = Post.objects.create(title=title, content=content, users=request.user)
        post.save()

        return redirect('post_detail_view', post.id)

def post_update_view(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == "GET":
        context = {
            'post': post
        }
        return render(request, 'post_update.html', context)     # post_update.html 만들어야 함.
    elif request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        post.title = title
        post.content = content
        post.save()

        return redirect('post_detail_view', post_id)

def post_delete_view(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == "GET":
        context = {
            'post': post
        }
        return render(request, 'post_delete.html', context)     # post_delete.html 만들어야 함.
    elif request.method == "POST":
        post.delete()
        return redirect('post_list_view')

def post_list_view(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post_list.html', context)       # post_list.html 만들어야 함.

def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'post_detail.html', context)
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post_creat(request):
    if request.method == "GET":
        return render(request, 'post_create_form.html')
    elif request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content, user=request.user)
        post.save()
        context = {
            'post': post
        }
        return render(request, 'post_detail.html', context)

def post_list_view(request):
    post_list = Post.objects.all()
    context = {
        'post_list': post_list,
    }
    return render(request, 'post_list.heml', context)

def post_serch_view(request):
    keyword = request.POST.get('keyword')
    result = Post.objects.filter(title__icontains=keyword).order_by('-created_at')
    context = {
        'keyword': keyword,
        'result': result
    }
    return render(request, 'post_search_result.html', context)

def post_update(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user == post.user:
        title = request.POST.get('title')
        content = request.POST.get('content')

        post.title = title
        post.content = content
        post.save()

        return render(request, 'post_detail.html', {'post': post})
    
    return HttpResponse("자신의 게시물만 수정할 수 있습니다.")

def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user == post.user:
        post.delete()
        return redirect('/post-list-url/')
    
    return HttpResponse("자신의 게시물만 삭제할 수 있습니다.")
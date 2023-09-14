
from django.http import HttpResponse
from django.shortcuts import render, redirect
from post.models import Post, Comment


# Create your views here.


def index(request):
    if request.method == 'GET':
        post = Post.objects.all()
        context = {
            'post': post,
        }
        return render(request, 'post/index.html', context)


def create(request):
    print(request.method)
    if request.method == 'GET':
        return render(request, 'post/create.html')
    elif request.method == 'POST':
        image = request.FILES.get('image')
        country = request.POST['country']
        city = request.POST['city']
        content = request.POST['content']
        Post.objects.create(
            image=image, country=country, city=city, content=content, user=request.user
        )
        return redirect('/post/')


def detail(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        comments = post.comment_set.all()
        print(comments)
        context = {
            'post': post,
            'comments': comments,
        }
        return render(request, 'post/detail.html', context)

    elif request.method == 'POST':
        post = Post.objects.get(id=post_id)
        user = request.user
        comment_form = request.POST['comment_form']
        Comment.objects.create(
            content=comment_form,
            post=post,
            user=user,
        )
        return redirect('/post/')


def update(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        context = {
            'post': post,
        }
        return render(request, 'post/update.html', context)
    elif request.method == 'POST':
        image = request.FILES.get('image')
        post = Post.objects.get(id=post_id)
        country = request.POST['country']
        city = request.POST['city']
        content = request.POST['content']
        is_completed = request.POST.get('is_completed', False)
        post.country = country
        post.city = city
        post.content = content
        post.is_completed = is_completed
        post.save()
        return redirect('/post/')


def delete(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        if request.user == post.user:
            post.delete()
            return redirect('/post/')
        else:
            return HttpResponse('권한이 없습니다.')


from django.http import HttpResponse
from django.shortcuts import render, redirect
from post.models import Post


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
        starting_date = request.POST['starting_date']
        finishing_date = request.POST['finishing_date']
        Post.objects.create(
            image=image, country=country, city=city, content=content, user=request.user, starting_date=starting_date, finishing_date=finishing_date
        )
        return redirect('/post/')


def detail(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        context = {
            'post': post,
        }
        return render(request, 'post/detail.html', context)


def update(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        context = {
            'post': post,
        }
        return render(request, 'post/update.html', context)
    elif request.method == 'POST':
        print(request.POST)
        image = request.FILES.get('image')
        post = Post.objects.get(id=post_id)
        country = request.POST['country']
        city = request.POST['city']
        content = request.POST['content']
        starting_date = request.POST['starting_date']
        finishing_date = request.POST['finishing_date']
        is_completed = request.POST.get('is_completed', False)
        post.country = country
        post.city = city
        post.content = content
        post.starting_date = starting_date
        post.finishing_date = finishing_date
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

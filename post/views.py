
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
        # Post 생성로직
        country = request.POST['country']
        city = request.POST['city']
        content = request.POST['content']
        Post.objects.create(
            country=country, city=city, content=content, user=request.user
        )
        return redirect('/post/')


def detail(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        context = {
            'post': post,
        }
        return render(request, 'post/detail.html', context)
    pass


def update(request):
    pass


def delete(request):
    pass

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import User

# Create your views here.


@csrf_exempt
def signup(request):
    print(request.method)
    if request.method == 'GET':
        return render(request, 'users/signup.html')
    elif request.method == 'POST':
        print(request.POST)
        User.objects.create_user(
            username=request.POST['username'], password=request.POST['password'], email=request.POST['email'])
        return redirect('/post/')


def login(request):
    print(request.method)
    if request.method == 'GET':
        return render(request, 'users/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/post/')
        else:
            return HttpResponse('로그인 실패')


def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('/post/')

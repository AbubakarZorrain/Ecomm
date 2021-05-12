from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def navbar(request):
    post = Post.objects.all()
    context = {'post':post}
    return render(request,'zblogapp/dashboard.html',context)

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, 'Login Sucessful')
            return redirect('/home/')
        else:
            messages.info(request, 'Username or Password Is Invalid.')

    return render(request, 'zblogapp/login.html')

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect( '/home/')

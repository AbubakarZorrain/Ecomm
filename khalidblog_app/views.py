from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.core import serializers
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
def arsha(request):
    product = Product.objects.all()
    context = {'product':product}
    return render(request, 'zblogapp/index.html',context)

def validate_username(request):
    username = request.GET.get('name', None)
    product = Product.objects.get(id=username)
    result = Product.objects.all()
    for size1 in result:
        a =size1.size.all()
    data1 = serializers.serialize('json', product.size.all())
    data = {
    'is_taken': Product.objects.all().filter(id=username).exists(),
    'name': product.name,
    'detail': product.detail,
    'price': product.price,
    'id': product.id,
    'image': product.product_image.url,
    'size':list(product.size.values_list("name", flat=True)),

    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'

        data['name2'] = 'hi...'

    return JsonResponse(data)

def cart_add(request):
    cart = Cart(request)
    username = request.GET.get('name', None)
    product = Product.objects.get(id=username)
    cart.add(product=product)
    data = {
        'is_taken': Product.objects.all().filter(id=username).exists(),
        'name': product.name,
        'detail': product.detail,
        'price': product.price,
        'id': product.id,
        'image': product.product_image.url

    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'

        data['name2'] = 'hi...'

    return JsonResponse(data)

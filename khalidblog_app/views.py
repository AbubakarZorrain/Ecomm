from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    post = Post.objects.all()
    context = {'post':post}
    return render(request,'khalidblog_app/index.html',context)

def post_detail(request,id):
    post = Post.objects.all().filter(id=id)
    post1 =Post.objects.get(id=id)
    comment = CommentReply.objects.all().filter(post=id)
    post2 = Post.objects.all().order_by('-id')[:3]
    if request.method == 'POST':
        comments = request.POST.get('comment')
        CommentReply.objects.create(
                post=post1, detail=comments, author = request.user)
    context = {'post': post, 'comment1': comment,'post1':post1,'post2':post2}
    return render(request,'khalidblog_app/full_detail.html',context)

def reply(request,id,pid):
    post1 = Post.objects.get(id=id)
    comment = CommentReply.objects.get(id=pid)
    comment1 = CommentReply.objects.all().filter(post=id)
    post2 = Post.objects.all().order_by('-id')[:3]
    context = {'comment': comment,'comment1':comment1, 'post1': post1,'post2':post2}
    if request.method == 'POST':
        comments = request.POST.get('comment')
        CommentReply.objects.create(
            post=post1, detail=comments,parent=comment, author=request.user)
        return render(request, 'khalidblog_app/full_detail.html', context)

    return render(request,'khalidblog_app/reply.html',context)
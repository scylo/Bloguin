from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    return render(request, 'base.html', locals())

def post_list(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'post_list.html', locals())

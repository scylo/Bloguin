from django.shortcuts import get_object_or_404, render
from .models import Post


def index(request):
    return render(request, 'base.html', locals())

def post_list(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'post_list.html', locals())


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    return render(request, 'post_detail.html', locals())

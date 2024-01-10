'''
dependendo da organização do projeto, as views devem ficar em arquivos separados
neste projeto, por simplicidade, as views ficam dentro do mesmo arquivo
'''
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views.decorators.cache import cache_page
from .models import Post
from .forms import PostForm


def index(request):
    return render(request, 'base.html', locals())

@login_required
@cache_page(60 * 15)
def post_list(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'post_list.html', locals())

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    return render(request, 'post_detail.html', locals())

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # dessa forma, salva autor de acordo com o escolhido no form
            post = form.save()
            
            # ou salva o usuário que está criando o post
            # (remover o campo 'author' do form)

            # cria o post sem salvar pois vamos fazer isso depois
            # post = form.save(commit=False)
            # post.author = request.user
            # post.save()
            return render(request, 'post_detail.html', locals())
    else:
        form = PostForm()
    return render(request, 'add_post.html', locals())

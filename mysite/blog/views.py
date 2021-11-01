from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

# Create your views here.
def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 2) # Tres postagens em cada página
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Se a pagina nao for um inteiro exibe a primeira
        posts = paginator.page(1)
    except EmptyPage:
        # Se a pagina estiver fora do intervalo
        # Exibe a ultima pagina de resultados
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
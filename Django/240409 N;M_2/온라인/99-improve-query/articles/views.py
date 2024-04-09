from django.shortcuts import render
from .models import Article, Comment
from django.db.models import Count


# Create your views here.
def index_1(request):
    # articles = Article.objects.order_by('-pk')
    # SQL의 Group b = annotate
    articles = Article.objects.annotate(Count('comment')).order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_1.html', context)


def index_2(request):
    # articles = Article.objects.order_by('-pk')
    # SQL의 INNER JOIN을 사용
    # 1:1 또는 N:1 참조 관계에서 사용
    articles = Article.objects.select_related('user').order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_2.html', context)


def index_3(request):
    # articles = Article.objects.order_by('-pk')
    # M:N 또는 N:1 역참조 관계에서 사용
    # SQL이 아닌 Python을 사용한 JOIN을 진행
    articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_3.html', context)


from django.db.models import Prefetch


def index_4(request):
    # articles = Article.objects.order_by('-pk')
    # articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
    articles = Article.objects.prefetch_related(
        Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
    ).order_by('-pk')

    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_4.html', context)

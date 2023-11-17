from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = Article.object.order_by('-published_at')
    context = {'ordering': ordering}
    return render(request, template, context)

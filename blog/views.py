from django.shortcuts import render
from .models import Article,Category
from django.views.generic import ListView


class HomeView(ListView):
    model = Article
    template_name = 'home.html'
    ordering = ['-created_date']


# def my_view(request):
#     articles = Article.objects.all()
#     return render(request, 'home.html', {'articles': articles})


def blog_view(request):
    category_list = Category.objects.all()
    article_list = Article.objects.all()
    return render(request, 'categories.html', {'category_list': category_list, 'article_list': article_list})

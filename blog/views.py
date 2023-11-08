from django.shortcuts import render
from .models import Article, Category
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator


class HomeView(ListView):
    model = Article
    template_name = 'home.html'
    ordering = ['-created_date']
    articles_per_page = 3

    def get(self, request, *args, **kwargs):
        article_list = Article.objects.all()
        paginator = Paginator(article_list, self.articles_per_page)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        context = {'page': page}
        return render(request, self.template_name, context)


class ArticleView(DetailView):
    model = Article
    template_name = 'article_details.html'


# def my_view(request):
#     articles = Article.objects.all()
#     return render(request, 'home.html', {'articles': articles})


def category_view(request):

    category_list = Category.objects.all()
    article_list = Article.objects.all()
    return render(request, 'categories.html', {'category_list': category_list, 'article_list': article_list})


def CategoryView(request, categories):

    category_query = Article.objects.filter(category__name=categories)
    paginator = Paginator(category_query, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'categories': categories.title(), 'category_query': category_query, 'page': page}
    return render(request, 'category_filter.html', context)


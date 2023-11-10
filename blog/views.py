from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .logreader import read_logs


class HomeView(ListView):
    model = Article
    template_name = 'home.html'
    ordering = ['-created_date']
    articles_per_page = 3

    def get(self, request, *args, **kwargs):
        last_read = ""
        article_list = Article.objects.filter(is_active=True)
        paginator = Paginator(article_list, self.articles_per_page)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

        log_file = 'access.log'

        with open(log_file, "r") as file:
            log_data = file.read()

        last_read = 13
        lines = log_data.split("\n")
        for line in lines:
            if line and line[-1].isdigit():
                last_read = line.split("/")[-1]
        last_article = Article.objects.get(id=last_read)

        context = {'page': page, 'last_read': last_read, 'last_article': last_article}
        return render(request, self.template_name, context)


class ArticleView(DetailView):
    model = Article
    template_name = 'article_details.html'


# def my_view(request):
#     articles = Article.objects.all()
#     return render(request, 'home.html', {'articles': articles})


def category_view(request):
    category_list = Category.objects.all()
    article_list = Article.objects.filter(is_active=True)
    return render(request, 'categories.html', {'category_list': category_list, 'article_list': article_list})


def CategoryFilterView(request, categories):
    category_query = Article.objects.filter(category__name=categories, is_active=True)
    paginator = Paginator(category_query, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'categories': categories.title(), 'category_query': category_query, 'page': page}
    return render(request, 'category_filter.html', context)

from django.shortcuts import render
from .models import Article
from django.views.generic import ListView


class HomeView(ListView):
    model = Article
    template_name = 'home.html'
    ordering = ['-created_date']

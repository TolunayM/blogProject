from django.urls import path
from .views import HomeView, ArticleView, category_view, CategoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cats/', category_view, name='cats'),
    path('article/<int:pk>', ArticleView.as_view(), name='article_details'),
    path('categories/<str:categories>/', CategoryView, name='categories'),
]

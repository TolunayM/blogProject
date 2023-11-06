from django.urls import path
from .views import HomeView,blog_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cats/',blog_view,name='cats')
]

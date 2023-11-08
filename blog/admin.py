from django.contrib import admin
from .models import Article, Category


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('is_active',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

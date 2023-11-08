from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    created_date = models.DateField()
    content = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title + " " + str(self.author)

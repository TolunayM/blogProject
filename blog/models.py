from django.db import models
from django.contrib.auth.models import User

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
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title + " " + str(self.author)

from django.db import models

# Create your models here.

class Post(models.Model):
    slug = models.CharField(max_length=200)
    image = models.ImageField()
    author = models.CharField(max_length=200)
    date = models.DateField()
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=500)
    content = models.TextField()

    def __str__(self):
        return f"title: {self.title}  \n author: {self.author}, \n content: {self.content} \n\n\n\n"
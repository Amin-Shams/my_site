from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email_address = models.EmailField()

class Tag(models.Model):
    caption = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=150)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=150, unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag)


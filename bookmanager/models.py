from django.db import models


# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=32)


class Bookinfo(models.Model):
    book_name = models.CharField(max_length=32)
    publister_id = models.ForeignKey(Publisher, on_delete=models.CASCADE, default='0')


class Author(models.Model):
    author_name = models.CharField(max_length=32)
    books = models.ManyToManyField('Bookinfo')

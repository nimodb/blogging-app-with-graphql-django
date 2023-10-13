from django.db import models
from django.utils.timezone import now

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    biodata = models.TextField()

    def __str__(self):
        return self.name

# Post Model


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateField(default=now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

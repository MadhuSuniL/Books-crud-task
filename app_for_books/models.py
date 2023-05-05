from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    pages_of_book = models.IntegerField(default=0)
    cover_image = models.FileField(upload_to='covers/')
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    content = RichTextField()
    description = RichTextField()
    time = models.DateField()
    picture = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

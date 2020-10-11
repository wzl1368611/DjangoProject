from django.contrib import admin
from Blog.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'time']


admin.site.register(Article, ArticleAdmin)
# Register your models here.

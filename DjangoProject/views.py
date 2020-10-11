import time

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse('hello world!')
    return render(request, 'index.html')


def page(request, id):
    # print('num的数据类型为', type(id))
    return HttpResponse('hello world url的参数是%s' % id)


def date(request, year, month, day):
    print(time.asctime())
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    print(time, month, day, '--------', type(year))
    times = time.struct_time(
        (int(year), int(month), int(day), 1, 1, 1, 1, 1, 1)
    )
    days = time.localtime(time.mktime(times))
    d = days.tm_yday
    print(type(d))
    return HttpResponse('它是%s 年的第%d天' % (year, d))


def base_new(request):
    return render(request, 'base_new.html')


from Blog.models import Article
import datetime


def selectHtml(request):
    # articles = Article.objects.all()
    articles = Article.objects.filter(author='author1')
    art = Article.objects.get(id=25)
    # art.title = '钢铁是怎么炼成的'
    # art.save()
    # art.delete()
    return render(request, 'selectHtml.html', locals())
    # for i in range(20):
    #     a = Article()
    #     a.title = 'book%d' % i
    #     if i % 3 == 0:
    #         a.author = 'author3'
    #     elif i % 3 == 1:
    #         a.author = 'author1'
    #     else:
    #         a.author = 'author2'
    #     a.time = datetime.datetime.now()
    #     a.content = 'hello world'
    #     a.description = 'hello world'
    #     a.picture = '1.jpg'
    #     a.save()


def template_example(request):
    data = {
        'name': 'james',
        'lists': [1, 2, 3, 4],
        'login_name': 'admin',
        'project': ['python', 'java', 'php', 'golang', 'js']

    }
    return render(request, 'template_example.html', locals())

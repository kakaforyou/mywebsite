#_*_ coding:utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from datetime import datetime
# Create your views here.
def home(request):
    return HttpResponse("hello,world, Django")

def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    str = {"文章标题=%s, }
def index(request):
    context = {
        'a': 'happy everyday',
        'b': 'fucking youself',
    }

    return render(request, 'index.html', context)
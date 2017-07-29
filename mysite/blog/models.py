#_*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField()

    created_time = models.DateTimeField(auto_now_add=True)
    modifield_time = models.DateTimeField(auto_now=True)
    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
# python_2_unicode_compatible 装饰器用于兼容 Python2
@python_2_unicode_compatible
class Category(models.Model):


    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Tag(models.Model):


    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):


    def __str__(self):
        return self.title

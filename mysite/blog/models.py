#_*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    article_name = models.CharField('文章标题', max_length=200) #文章标题
    published_time = models.DateTimeField('发布时间', auto_now_add=True) #发布时间
    last_published_time = models.DateTimeField('修改时间', auto_now=True)#修改时间
    catagory = models.CharField('文章标签', max_length=200, blank=True)#文章标签
    content = models.TextField('文章内容', blank=True, null=True)#文章内容

    def __unicode__(self):
        return self.article_name

    class Meta: #按时间下降排序
        ordering = ['-last_published_time']

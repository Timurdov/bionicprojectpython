# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
    article_title = models.CharField(max_length = 200)
    article_text = models.TextField()
    article_data = models.DateTimeField()
    article_likes = models.IntegerField(default=0)

    def __unicode__(self):
        return "%s" %(self.article_title)

class Comments(models.Model):
    class Meta():
        db_table = 'comments'
    comments_date = models.DateTimeField(auto_now=False,auto_now_add=True)
    comments_text = models.TextField(verbose_name="Ваши комментарии:")
    comments_article = models.ForeignKey(Article)
    comments_from = models.ForeignKey(User)
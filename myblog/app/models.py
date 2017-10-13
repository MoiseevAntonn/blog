# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    about_mr = models.TextField()
    name = models.CharField(max_length=40)

class Post(models.Model):
    author = models.ForeignKey(User)
    body = models.TextField()
    title = models.CharField(max_length=40)

class Comment(models.Model):
    author = models.CharField(max_length=40)
    post = models.ForeignKey(Post)
    title = models.CharField(max_length=40)

class Tag(models.Model):
    name = models.ManyToManyField(Post)




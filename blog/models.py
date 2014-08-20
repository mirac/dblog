# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(auto_created=True)
    description = models.TextField()
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey('Category')
    tags = models.ManyToManyField('Tag')
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(auto_created=True)
    description = models.TextField()

    def __unicode__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name


class Setting(models.Model):
    site_title = models.CharField(max_length=255)
    site_description = models.TextField(max_length=300)
    footer_description = models.CharField(max_length=255)
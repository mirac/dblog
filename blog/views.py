# -*- coding: utf-8 -*-
import re

from django.db.models import Q
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from blog.models import Post, Category, Tag, Setting


settings = Setting.objects.last()
categories = Category.objects.all().reverse()
tags = Tag.objects.all()


def index(request):
    posts = Post.objects.all().order_by("-created_date")

    return render_to_response("index.html", {
        "posts": posts,
        # Defaults
        "categories": categories,
        "settings": settings
    }, RequestContext(request))


def post_view(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render_to_response("post_view.html", {
        "post": post,
        # Defaults
        "categories": categories,
        "settings": settings
    }, RequestContext(request))


def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category).all() \
        .order_by("-created_date")

    return render_to_response("category_view.html", {
        "category": category,
        # Defaults
        "categories": categories,
        "posts": posts,
        "settings": settings
    })


def tag_view(request, slug):
    pass
    """
    post_db = Post.objects.all()
    posts = []

    for post in post_db:
        if slug in post.tags.all():
            posts.append(post)

    return render_to_response("tag_view.html", {
        "posts": posts,
        # Defaults
        "categories": categories,
        "settings": settings
    }, RequestContext(request))
    """


def search(request):
    keyword = request.GET["keyword"]
    result = Post.objects.filter(Q(title__icontains=keyword)).order_by('-modified_date')

    return render_to_response("search.html", {
        "result": result,
        "keyword": keyword,
        # Defaults
        "categories": categories,
        "settings": settings
    }, RequestContext(request))
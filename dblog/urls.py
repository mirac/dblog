import os
from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

 # SLUG defination

STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')

urlpatterns = patterns('',

    url(r'^$', 'blog.views.index'),
    url(r'^index.html$', 'blog.views.index', name='index'),

    url('^view/(?P<slug>[\w\d-]+).html$', 'blog.views.post_view', name='post_view'),

    url('^category/(?P<slug>[\w\d-]+).html$', 'blog.views.category_view', name='cat_view'),

    url('^tag/(?P<slug>[\w\d-]+).html$', 'blog.views.tag_view', name='tag_view'),

    url(r'^search.html$', 'blog.views.search'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT }),
)


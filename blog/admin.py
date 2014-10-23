# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'published',
        'title',
        'created',
    )
    list_filter = ('author', 'published', 'created')
admin.site.register(BlogPost, BlogPostAdmin)

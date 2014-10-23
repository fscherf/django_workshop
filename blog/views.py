from django.shortcuts import render
from models import BlogPost

def view_posts(request, post_id=None):
    if post_id:
        try:
            posts = [BlogPost.objects.get(id=post_id, published=True)]
        except BlogPost.DoesNotExist:
            posts = None
    else:
        posts = BlogPost.objects.all()

    return render(
        request,
        'view_posts.html',
        {
            'posts': posts,
        }
    )

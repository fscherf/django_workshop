from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from models import BlogPost
from forms import BlogPostForm

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

@login_required
def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)

        if form.is_valid():
            new_post = BlogPost(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                published=True,
                author=request.user
            )

            new_post.save()

            return redirect('view_posts', post_id=new_post.id)
    else:
        form = BlogPostForm()

    return render(
        request,
        'add_post.html',
        {
            'form': form,
        }
    )

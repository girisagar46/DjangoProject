from django.shortcuts import render
from .models import Post


def articles(request):
    posts = Post.objects.filter(is_published=True)

    ctx = {
        "posts": posts
    }

    return render(request,
                  template_name='blog/blog_index.html',
                  context=ctx)

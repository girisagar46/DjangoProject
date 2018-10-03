from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


def articles(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_date')

    ctx = {
        "posts": posts
    }

    return render(request,
                  template_name='blog/blog_index.html',
                  context=ctx)


def create_article(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        user = request.user

        post = Post.objects.create(title=title, body=body, author=user, is_published=True)

        return redirect('blog_index')

    return render(request,
                  template_name='blog/blog_create.html',
                  context={})


def blog_detail(request, post_id):
    #post = Post.objects.get(id=post_id)
    # post = get_object_or_404(Post, id=post_id)
    post = Post.objects.filter(id=post_id).first()

    ctx = {
        "post": post
    }

    return render(request, template_name='blog/blog_detail.html', context=ctx)

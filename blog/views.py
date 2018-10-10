from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import Post, Comments


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

        return redirect(to='blog_index')

    return render(request,
                  template_name='blog/blog_create.html',
                  context={})


def blog_detail(request, post_id):
    #post = Post.objects.get(id=post_id)
    # post = get_object_or_404(Post, id=post_id)
    post = Post.objects.filter(id=post_id).first()

    comments = Comments.objects.filter(post=post)

    ctx = {
        "post": post,
        "comments": comments
    }

    return render(request, template_name='blog/blog_detail.html', context=ctx)


def add_comment(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        comment_body = request.POST.get("comment_body")
        post_id = request.POST.get("post_id")

        post = Post.objects.get(id=post_id)

        comment = Comments.objects.create(email=email,
                                          comment_body=comment_body,
                                          post=post)

        return redirect(to='blog_detail', post_id=post_id)


def like_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.num_likes += 1
        post.save()

        return JsonResponse({"new_likes_count": post.num_likes})

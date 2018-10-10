from django.urls import path

from blog.views import articles, create_article, blog_detail, add_comment, like_post

urlpatterns = [
    path('', articles, name='blog_index'),
    path('create/', create_article, name='blog_create'),
    path('detail/<int:post_id>', blog_detail, name='blog_detail'),
    path('add-comment/', add_comment, name='add_comment'),
    path('like/<int:post_id>', like_post, name='like_post')
]
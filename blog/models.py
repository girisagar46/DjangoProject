from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)
    num_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title + self.author.username


class Comments(models.Model):
    email = models.EmailField(max_length=30)
    comment_body = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.email + " - " + str(self.post.id)
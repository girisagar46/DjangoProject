from django.template import Library
from django.db.models import Count

from ..models import Post

register = Library()

@register.simple_tag
def post_count():
    return Post.objects.count()


@register.inclusion_tag("blog/latest_posts.html")
def get_latest(count=3):
    latest_post = Post.objects.order_by("-published_date")[:count]
    return {"latest_posts": latest_post}


@register.simple_tag
def get_popular(count=3):
    popular = Post.objects.annotate(
        total_comment=Count('comments')
    ).order_by('-total_comment')[:count]
    return popular


@register.filter(name='my_filter')
def to_upper(text):
    return text.upper()
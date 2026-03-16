from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Post.objects.filter(active=True).order_by('-created')

    def location(self, post):
        return f'/post/{post.slug}/'

    def lastmod(self, post):
        return post.created


class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return ['home', 'posts']

    def location(self, item):
        return reverse(item)
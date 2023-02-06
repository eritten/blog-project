from django.contrib.sitemaps import Sitemap
from .models import Post


class SongMap(Sitemap):
    changefreq = 'daily'
    priority = 1.0
    def items(self):
        return Post.objects.all()
    def lastmod(self, obj):
        return obj.created_at
    def location(self, obj):
        return obj.get_absolute_url()

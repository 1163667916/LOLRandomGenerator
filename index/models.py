from django.db import models

# Create your models here.
class Site(models.Model):
    site_link = models.CharField(max_length=200, verbose_name='网站链接')
    site_name = models.CharField(max_length=200, verbose_name='网站名称')
    order = models.IntegerField(default=0, verbose_name='顺序')

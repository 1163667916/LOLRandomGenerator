from datetime import datetime

from django.db import models

# Create your models here.


class Photos(models.Model):
    nickname = models.CharField(
        default='', max_length=255, verbose_name='展示的昵称')
    filename = models.CharField(
        default='', max_length=255, verbose_name='文件名称')
    filepath = models.CharField(
        default='', max_length=255, verbose_name='文件路径')
    size = models.IntegerField(default=0, verbose_name='大小')
    width = models.IntegerField(default=0, verbose_name='宽度')
    height = models.IntegerField(default=0, verbose_name='高度')
    disabled = models.BooleanField(default=False, verbose_name='不可见')
    created_at = models.DateTimeField(
        default=datetime.now, verbose_name='创建时间')


class Sorts(models.Model):
    title = models.CharField(
        default='', max_length=255, verbose_name='标题')
    key = models.CharField(default='', max_length=255, verbose_name='key')
    order = models.IntegerField(default=0, verbose_name='顺序')
    photo = models.ManyToManyField(to='Photos')
    created_at = models.DateTimeField(
        default=datetime.now, verbose_name='创建时间')

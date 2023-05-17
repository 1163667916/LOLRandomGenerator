from django.db import models

# Create your models here.


class VideoInfo(models.Model):
    title = models.CharField(default='', max_length=255, verbose_name='视频标题')
    video_path = models.CharField(
        default='', max_length=255, verbose_name='视频路径')
    cover_path = models.CharField(
        default='', max_length=255, verbose_name='封面路径')


class FileViewer(models.Model):
    file_path = models.CharField(
        default='', max_length=255, verbose_name='文件路径')
    qr_code_path = models.CharField(
        default='', max_length=255, verbose_name='二维码路径')
    file_type = models.CharField(
        default='', max_length=255, verbose_name='文件类型')

# from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'upload'
urlpatterns = [
    path(r'upload_video', views.upload_video),
    path(r'upload_viewer_file', views.upload_img)
]

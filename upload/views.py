import json
import traceback
import time
import datetime
import qrcode
import os

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from frontend.decorator.post_only import post
from .models import VideoInfo, FileViewer
from frontend.utils.file import FileTool


video_save_path = 'video_files/'
cover_save_path = 'cover_files/'

video_file_tool = FileTool(video_save_path)
cover_file_tool = FileTool(cover_save_path)


def getExt(_str: str):
    dot_idx = _str.rfind('.')
    return (_str[0:dot_idx], _str[dot_idx:])


def save_file(file, file_tool):
    try:
        filename, ext = getExt(file.name)
        _time = time.time()
        _date = datetime.date.fromtimestamp(_time)
        _dir = f'{_date.year}/{_date.month}/{_date.day}'
        format_filename = f'{int(_time * 1000)}{ext}'
        file_tool.write_file(
            _dir,
            format_filename, file
        )
        return f'{_dir}/{format_filename}'
    except:
        print(traceback.format_exc())
        return False

# Create your views here.


@post
def upload_video(request: HttpRequest):
    print('upload_video')
    try:
        body = request.POST
        title = body.get('title', None)
        cover_file = request.FILES['cover']
        video_file = request.FILES['x-video']

        if not title or not cover_file or not video_file:
            return HttpResponse(json.dumps({'code': 0, 'msg': '缺少必要参数', 'data': {}}))

        save_file(cover_file, cover_file_tool)
        save_file(video_file, video_file_tool)

        # video_info = VideoInfo(title=title, cover='', video='')
        # video_info.save()
    except:
        print(traceback.format_exc())

    return HttpResponse(json.dumps({'code': 1, 'msg': '11111', 'data': {}}))


@post
def connect_socket(request: HttpRequest):
    pass


viewer_path_file = 'file_viewer/file'
viewer_path_qrcode = 'file_viewer/qrcode'
file_viewer_tool = FileTool(viewer_path_file)
qrcode_viewer_tool = FileTool(viewer_path_qrcode)


@post
def upload_img(request: HttpRequest):
    from frontend import GlobalData
    img_file = None
    try:
        img_file = request.FILES['x-file']
    except:
        return HttpResponse(json.dumps({'code': 0, 'msg': 'not file uploaded', 'data': {}}))
    from frontend.utils.common import hash_name, store_static_path
    filename, ext = getExt(img_file.name)
    print(time.time())
    print(time.time() * 1000)
    filename = hash_name(
        f'{filename}-{int(time.time() * 1000)}').hexdigest() + '.png'
    print(filename)
    saved_path = save_file(img_file, file_viewer_tool)
    if saved_path:
        print(viewer_path_file, saved_path)

        url = '{host}/statics/{dir}/{filename}'.format(
            host=GlobalData.LOCAL_HOST, dir=viewer_path_file, filename=saved_path)
        qrcode_storage_url = store_static_path(
            f'{viewer_path_qrcode}/{filename}')
        qrcod_access_url = '{0}/statics/{1}'.format(GlobalData.LOCAL_HOST,
                                                    f'{viewer_path_qrcode}/{filename}')
        qrcode_img = qrcode.make(url)
        qrcode_img.save(qrcode_storage_url)

    return HttpResponse(json.dumps({'code': 1, 'msg': 'success', 'data': {'url': qrcod_access_url}}))

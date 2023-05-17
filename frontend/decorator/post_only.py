import json
from django.http import HttpResponse

def post(fn):
  def wrapper(request, *arg, **kwargs):
    print(request.method)
    if request.method != 'POST':
      print('jiniiiiiii')
      return HttpResponse(json.dumps({'code': 0, 'msg': f'request method error: {request.method}'}))
    return fn(request, *arg, **kwargs)
  return wrapper
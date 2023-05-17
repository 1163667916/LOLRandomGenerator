import requests

from django.shortcuts import render
from django.http import HttpResponse


from .models import Site

import json

# Create your views here.
def get_site_link(request):
    # result = json.dumps(Site.objects.all())
    result = Site.objects.all()
    print(result)
    return HttpResponse('success')

def post_site(request):
    print(request)
    site_name = request.POST['site_name']
    site_link = request.POST['site_link']
    print(site_name, site_link)
    try:
        Site.objects.create(site_name=site_name, site_link=site_link)
    except:
        pass
    return HttpResponse('success')
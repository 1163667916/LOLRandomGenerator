from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
page_url = 'https://www.op.gg/champions?region=global&tier=platinum_plus'

# api
champions_url = 'https://op.gg/api/v1.0/internal/bypass/meta/champions?hl=zh_CN'

def request_legend_list(request):
  print('1111')
  response = requests.get(champions_url, headers={
      'user-agent': User_Agent,
  })
  html = response.text
  print(response.json)
  return HttpResponse(response.text)
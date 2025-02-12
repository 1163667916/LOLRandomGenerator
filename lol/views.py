import random
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.template import loader
import requests
import json
import os
from bs4 import BeautifulSoup

from .helper.data_fetcher import PlayerFetcher
from frontend.settings import BASE_DIR

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


# GET /lol-match-history/v1/games/{gameId}

def fetch_data(request: HttpRequest):
  # summoner = request.GET.get("summoner")
  # if not summoner:
  #   return HttpResponse("not summoner")
  # player = PlayerFetcher(summoner)
  # player.run()
  
  return HttpResponse("ok")


CHAMPION_DATA_PATH = os.path.join(BASE_DIR, "py", "champions.json")
RUNE_DATA_PATH = os.path.join(BASE_DIR, "py", "rune.json")
POSITION_DATA_PATH = os.path.join(BASE_DIR, "py", "position.json")
SUMMONER_SKILL_DATA_PATH = os.path.join(BASE_DIR, "py", "summonerSkill.json")
BACKGROUND_IMAGE_PATH = os.path.join(BASE_DIR, "py", "bg")

def read_file(filepath):
  if os.path.exists(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
      data = json.loads(f.read())
    return data

def random_champion(request: HttpRequest):
  print("CHAMPION_DATA_PATH", CHAMPION_DATA_PATH)
  championData = read_file(CHAMPION_DATA_PATH)
  runeData = read_file(RUNE_DATA_PATH)
  posData = read_file(POSITION_DATA_PATH)
  summonerSkillData = read_file(SUMMONER_SKILL_DATA_PATH)
  
  bg_list = os.listdir(BACKGROUND_IMAGE_PATH)
  bg = random.choice(bg_list)

  template = loader.get_template("lol/random_champion.html")

  context = {
    "champions": championData,
    "runeData": runeData,
    "positionData": posData,
    "summonerSkillData": summonerSkillData,
    "backgroundFile": bg,
  }

  return HttpResponse(template.render(context, request))

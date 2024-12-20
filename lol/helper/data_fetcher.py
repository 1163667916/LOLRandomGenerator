import requests
from lol.models import Game, GameDetail, Player


# 用管理员CMD执行 wmic PROCESS WHERE name='LeagueClientUx.exe' GET commandline
# 找到 –remoting-auth-token 和 –app-port 
# 替换下面两个参数的值
token = 'dj0Yg05sLKPxfrhOsu8cHA'
port = '14998'
base_url = 'https://riot:' + token + '@127.0.0.1:' + port

class Server(object):
  def __init__(self) -> None:
    pass

  @staticmethod
  def get_summoner(summoner):
    url = base_url + '/lol-summoner/v1/summoners'
    resp = requests.get(url, data={'name': summoner}, verify=False)
    print("get_summoner", resp.json())
    return resp.json()

  @staticmethod
  def get_match_history(uuid, begIndex, endIndex):
    url = base_url + '/lol-match-history/v1/products/lol/' + str(uuid) + f'/matches?begIndex={begIndex}&endIndex={endIndex}'
    resp = requests.get(url, data={}, verify=False)

class PlayerFetcher(object):
  def __init__(self, summoner:str) -> None:
    self.summoner = summoner

  def fetch(self):
    self.result = Server.get_summoner(self.summoner)

  def check(self):
    self.player_data = {}
    if self.result:
      self.player_data["gameName"] = self.result.get("gameName")
      self.player_data["puuid"] = self.result.get("puuid")
      self.player_data["summonerId"] = self.result.get("summonerId")
      self.player_data["summonerName"] = self.result.get("displayName")

      self.check_pass = True
      return
    self.check_pass = False

  def save(self):
    if self.check_pass:
      p = Player(**self.player_data)
      p.save()

  def run(self):
    self.fetch()
    self.check()
    self.save()


class GameFetcher(object):
  def __init__(self, puuid: str) -> None:
    self.puuid = puuid

  def fetch(self):
    startIndex = 0
    endIndex = 100
    Server.get_match_history(self.puuid, startIndex, endIndex)
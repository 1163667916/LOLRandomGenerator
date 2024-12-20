import datetime
import json
import requests

requests.packages.urllib3.disable_warnings()


# 用管理员CMD执行 wmic PROCESS WHERE name='LeagueClientUx.exe' GET commandline
# 找到 –remoting-auth-token 和 –app-port 
# 替换下面两个参数的值
token = 'IXmrWOwgsu8w-KhhvC569Q'
port = '1709'

base_url = 'https://riot:' + token + '@127.0.0.1:' + port


def get_items():
  url = base_url + '/lol-loot/v1/loot-items'
  resp = requests.get(url, verify=False)
  print("get_items", resp.json())
  return resp.json()


def main():
  get_items()


if __name__ == "__main__":
  main()
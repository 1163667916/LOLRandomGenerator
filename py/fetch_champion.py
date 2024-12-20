import os
import requests
import json

User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
champions_url = 'https://op.gg/api/v1.0/internal/bypass/meta/champions?hl=zh_CN'

file_path = os.path.join(os.path.dirname(__file__), "champions.json")
image_path = os.path.join(os.path.dirname(__file__), "images")

if not os.path.exists(image_path):
  os.makedirs(image_path)

def main():
  response = requests.get(champions_url, headers={
      'user-agent': User_Agent,
  })

  if not response.status_code == 200:
    return
  
  data = response.json().get("data", [])

  res = []
  
  for item in data:
    # print(item)
    id = item.get("id")
    name = item.get("name")
    image_url = item.get("image_url")
    key = item.get("key")

    r = requests.get(image_url)
    if r.status_code == 200:
      with open(os.path.join(image_path, f"{id}_{key}.png"), "wb") as png:
        png.write(r.content)
      
    res.append({
      "id": id,
      "name": name,
      "key": key,
    })

  with open(file_path, "w+", encoding="utf-8") as f:
    f.write(json.dumps(res, indent=4, ensure_ascii=False))

if __name__ == "__main__":
  main()
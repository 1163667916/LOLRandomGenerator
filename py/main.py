import random

lines = ["上路", "打野", "中路", "下路", "辅助"]

players = ["驴", "莫", "胡", "高", "曾"]

videoTime = [i + 1 for i in range(71)]

for i in range(5):
  l = random.choice(lines)
  lines.remove(l)
  
  p = random.choice(players)

  v = random.choice(videoTime)
  players.remove(p)

  print("人:", p, "玩", l, "视频：", v, "秒")



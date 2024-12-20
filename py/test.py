import asyncio
import websockets
import json

async def get_lol_equipment():
    # 连接到《英雄联盟》客户端提供的 WebSocket 服务
    url = "ws://127.0.0.1:1709/liveclientdata/allgamedata"
    
    try:
        # 建立 WebSocket 连接
        async with websockets.connect(url) as websocket:
            # 等待客户端返回的数据
            data = await websocket.recv()
            
            # 解析返回的 JSON 数据
            game_data = json.loads(data)
            
            # 获取所有玩家的信息
            for player in game_data.get('players', []):
                summoner_name = player.get('summonerName', 'Unknown')
                print(f"玩家 {summoner_name} 的装备信息：")
                items = player.get('items', [])
                
                # 输出玩家的装备列表
                if not items:
                    print("  没有装备")
                for item in items:
                    item_name = item.get('name', 'Unknown Item')
                    print(f"  - {item_name}")
                
                print()

    except Exception as e:
        print(f"发生错误：{e}")

# 运行 WebSocket 连接并获取数据
asyncio.run(get_lol_equipment())
import requests
import json

def load_config():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def send_webhook(news_items):
    config = load_config()
    webhook_url = config['webhook_url']
    
    for item in news_items:
        embed = {
            "embeds": [
                {
                    "title": item['title'],
                    "description": f"來源: {item['source']}",
                    "url": item['link'],
                    "color": 0xffffff,  # 可選，顏色可以根據需要更改
                    # "footer": {  # 刪除這一行以去掉底部文字
                    #     "text": "這是底部文字"  # 可選，底部文字
                    # },
                    "image": {
                        "url": item.get('image_url', '')  # 添加圖片 URL
                    }
                }
            ]
        }
        
        response = requests.post(
            webhook_url,
            data=json.dumps(embed),
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code != 204:
            print(f"發送 webhook 失敗: {response.status_code}, {response.text}")

# 使用範例
if __name__ == "__main__":
    # 假設這是您要發送的新聞項目
    news_items = [
        {
            "source": "動區動趨",
            "title": "輝達AI模型再發功：精準預測「山陀兒」詭異路徑",
            "link": "https://www.blocktempo.com/nvidias-ai-model-strikes-again-accurately-predicts-typhoon-path/",
            "image_url": "https://image.blocktempo.com/2024/10/ai-1.webp"  # 添加圖片 URL
        }
    ]
    send_webhook(news_items)
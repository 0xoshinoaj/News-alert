import requests
import json

def load_config():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def send_webhook(news_items):
    config = load_config()
    webhook_url = config['webhook_url']
    
    for item in news_items:
        payload = {
            "content": f"【{item['source']}】{item['title']} {item['link']}"
        }
        
        response = requests.post(
            webhook_url,
            data=json.dumps(payload),
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code != 204:
            print(f"發送 webhook 失敗: {response.status_code}, {response.text}")
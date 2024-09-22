import time
import json
import importlib
from webhook_sender import send_webhook
from utils.memory import update_memory

def load_config():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    config = load_config()
    print("程式開始運行...")
    while True:
        print("開始爬取新聞...")
        all_news_items = []
        for website in config['websites']:
            print(f"正在爬取 {website['name']} 的新聞 (URL: {website['url']})...")
            try:
                scraper_module = importlib.import_module(f"scrapers.{website['scraper']}")
                site_news = scraper_module.scrape(website['url'], website['name'])
                all_news_items.extend(site_news)
                print(f"從 {website['name']} 爬取到 {len(site_news)} 條新聞")
            except Exception as e:
                print(f"爬取 {website['name']} 時發生錯誤: {str(e)}")

        if all_news_items:
            unsent_news = update_memory(all_news_items)
            if unsent_news:
                print(f"找到 {len(unsent_news)} 條新聞，準備發送...")
                send_webhook(unsent_news)
            else:
                print("沒有新的新聞需要發送。")
        else:
            print("沒有找到新聞。")
        print("等待下一次執行...")
        time.sleep(60)  # 等待60秒

if __name__ == "__main__":
    main()
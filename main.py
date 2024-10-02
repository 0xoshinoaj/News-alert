import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
import json
from webhook_sender import send_webhook
from utils.memory import update_memory, load_sent_articles
from scrapers.generic_scraper import scrape

VERSION = "1.2.2"

def load_config():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    config = load_config()
    print("程式開始運行...")
    while True:
        print("開始搜尋新聞...")
        all_news_items = []
        sent_articles = load_sent_articles()
        for website in config['websites']:
            print(f"正在更新【 {website['name']} 】的文章 (URL: {website['url']})...")
            try:
                site_news = scrape(website['url'], website['name'])
                print(f"爬取到的文章數量: {len(site_news)}")
                new_articles = [article for article in site_news if article['link'] not in sent_articles]
                print(f"新文章數量: {len(new_articles)}")
                all_news_items.extend(new_articles)
                print(f"從【 {website['name']} 】發現了 {len(site_news)} 條文章，新聞 {len(new_articles)} 篇")
                
                # 輸出所有新文章的鏈接
                for article in new_articles:
                    print(f"新文章連結: {article['link']}")

            except Exception as e:
                print(f"搜尋 {website['name']} 時發生錯誤: {str(e)}")

        if all_news_items:
            unsent_news = update_memory(all_news_items)
            if unsent_news:
                print(f"發現了 {len(unsent_news)} 條新聞，準備發送...")
                for news in unsent_news:
                    print(f"準備發送: {news['link']}")
                send_webhook(unsent_news)
            else:
                print("沒有新聞需要發送。")
        else:
            print("沒有新聞。")
        print("等待下一次執行...5分鐘後更新...")
        time.sleep(300)  # 等待5分鐘

if __name__ == "__main__":
    main()
import requests
from bs4 import BeautifulSoup
import time
import json
import os

def load_config():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def load_sent_articles():
    if os.path.exists('sent_articles.json'):
        with open('sent_articles.json', 'r') as f:
            return set(json.load(f))
    return set()

def save_sent_articles(sent_articles):
    with open('sent_articles.json', 'w') as f:
        json.dump(list(sent_articles), f)

def scrape_news():
    config = load_config()
    news_items = []
    sent_articles = load_sent_articles()
    
    print(f"開始爬取 {len(config['websites'])} 個網站...")
    
    for site in config['websites']:
        print(f"正在爬取: {site['name']} ({site['url']})")
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(site['url'], headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            articles = soup.find_all('h3', class_='jeg_post_title')
            print(f"在 {site['name']} 找到 {len(articles)} 篇文章")
            
            new_articles_count = 0
            for article in articles:
                link_element = article.find('a')
                if link_element:
                    title = link_element.text.strip()
                    link = link_element['href']
                    if link not in sent_articles:
                        news_items.append({
                            'source': site['name'],
                            'title': title,
                            'link': link
                        })
                        sent_articles.add(link)
                        new_articles_count += 1
                        print(f"新增文章: {title}")
            
            print(f"新增 {new_articles_count} 篇新文章")
            
            time.sleep(2)  # 在每個網站之間添加短暫延遲
        except Exception as e:
            print(f"爬取 {site['name']} 時發生錯誤: {str(e)}")
    
    save_sent_articles(sent_articles)
    print(f"爬取完成，共找到 {len(news_items)} 條新聞")
    return news_items
import json
import os

MEMORY_FILE = 'sent_articles.json'

def load_sent_articles():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
            return set(json.load(f))
    return set()

def save_sent_articles(sent_articles):
    with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(list(sent_articles), f)

def update_memory(new_articles):
    sent_articles = load_sent_articles()
    unsent_articles = [article for article in new_articles if article['link'] not in sent_articles]
    sent_articles.update(article['link'] for article in unsent_articles)
    save_sent_articles(sent_articles)
    return unsent_articles
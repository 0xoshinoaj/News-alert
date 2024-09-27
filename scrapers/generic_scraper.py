import time
from utils.http_utils import get_page
from utils.data_processing import extract_articles

def scrape(url, source):
    soup = get_page(url)
    articles = extract_articles(soup, source)
    
    # 為每篇文章添加時間戳
    current_time = int(time.time())
    for article in articles:
        article['timestamp'] = current_time
    
    return articles

# 刪除了 write_to_file 函數和其他未使用的內容
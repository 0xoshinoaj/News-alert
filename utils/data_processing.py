from utils.http_utils import get_preview_image  # 引入新函數

def extract_articles(soup, source):
    articles = []
    seen_links = set()  # 用於追踪已經見過的鏈接
    seen_titles = set()  # 用於追踪已經見過的標題

    def process_elements(elements):
        for element in elements:
            link_element = element.find('a')
            if link_element:
                title = link_element.text.strip()
                link = link_element['href']
                
                # 檢查這個鏈接和標題是否已經被處理過
                if link not in seen_links and title not in seen_titles:
                    seen_links.add(link)
                    seen_titles.add(title)
                    articles.append({'source': source, 'title': title, 'link': link})  # 只添加 link 和 title

    if source == '動區動趨':
        elements = soup.find_all('article', class_='jeg_post jeg_pl_md_2 format-standard')
        for article in elements:
            process_elements([article.find('h3', class_='jeg_post_title')])

    elif source == '鏈新聞':
        loop_posts = soup.find_all('div', class_='loop-post')
        for loop_post in loop_posts:
            elements = loop_post.find_all('h3', class_='title')
            process_elements(elements)

    elif source == '區塊客':
        elements = soup.find_all('article', class_='jeg_post jeg_pl_md_1 format-standard')
        for article in elements:
            process_elements([article.find('h3', class_='jeg_post_title')])
        
        elements = soup.find_all('article', class_='jeg_post jeg_pl_lg_box format-standard')
        for article in elements:
            process_elements([article.find('h3', class_='jeg_post_title')])

    elif source == '桑幣區識':
        elements = soup.find_all('h3', class_='post-title max-two-lines')
        process_elements(elements)

    return articles
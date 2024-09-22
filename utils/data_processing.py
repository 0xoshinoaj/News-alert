def extract_articles(soup, source):
    articles = []
    if source == '動區動趨':
        elements = soup.find_all('h3', class_='jeg_post_title')
    elif source == '鏈新聞':
        elements = soup.find_all('h3', class_='title')
    elif source == '區塊客':
        elements = soup.find_all('h3', class_='jeg_post_title')  # 請根據實際情況調整
    elif source == '桑幣區識':
        elements = soup.find_all('h3', class_='post-title max-two-lines')  # 請根據實際情況調整
    else:
        return articles  # 如果是未知來源，返回空列表

    for element in elements:
        link_element = element.find('a')
        if link_element:
            title = link_element.text.strip()
            link = link_element['href']
            articles.append({'source': source, 'title': title, 'link': link})
    return articles
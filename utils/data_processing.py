def extract_articles(soup, source):
    articles = []
    if source == 'BlockTempo':
        elements = soup.find_all('h3', class_='jeg_post_title')
    elif source == 'ABMedia':
        elements = soup.find_all('h3', class_='title')
    else:
        return articles  # 如果是未知來源，返回空列表

    for element in elements:
        link_element = element.find('a')
        if link_element:
            title = link_element.text.strip()
            link = link_element['href']
            articles.append({'source': source, 'title': title, 'link': link})
    return articles
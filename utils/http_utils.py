import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random

# 初始化 UserAgent
ua = UserAgent()

def load_proxies(filename='proxy.txt'):
    proxies = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:  # 確保行不為空
                parts = line.split(':')
                if len(parts) == 5:
                    ip, port, username, password, proxy_type = parts
                    proxy = {
                        'host': ip,
                        'port': int(port),
                        'username': username,
                        'password': password,
                        'proxy_type': proxy_type.lower()
                    }
                    proxies.append(proxy)
    return proxies

def get_random_proxy(proxies):
    return random.choice(proxies) if proxies else None

def get_page(url):
    proxies = load_proxies()  # 加載代理
    proxy = get_random_proxy(proxies)  # 隨機選擇一個代理

    headers = {
        'User-Agent': ua.random  # 隨機生成 User-Agent
    }

    # 構建代理字典
    if proxy:
        if proxy['proxy_type'] == 'socks5':
            proxy_dict = {
                'http': f'socks5://{proxy["username"]}:{proxy["password"]}@{proxy["host"]}:{proxy["port"]}',
                'https': f'socks5://{proxy["username"]}:{proxy["password"]}@{proxy["host"]}:{proxy["port"]}'
            }
        else:  # http or https
            proxy_dict = {
                'http': f'http://{proxy["username"]}:{proxy["password"]}@{proxy["host"]}:{proxy["port"]}',
                'https': f'http://{proxy["username"]}:{proxy["password"]}@{proxy["host"]}:{proxy["port"]}'
            }
    else:
        proxy_dict = None

    response = requests.get(url, headers=headers, proxies=proxy_dict)
    return BeautifulSoup(response.text, 'html.parser')

def get_preview_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 確保請求成功

        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找 Open Graph 標籤
        og_image = soup.find('meta', property='og:image')
        if og_image:
            return og_image['content']  # 返回圖片 URL
        else:
            print("未找到 Open Graph 圖片標籤")
            return None
    except Exception as e:
        print(f"獲取預覽圖片時發生錯誤: {e}")
        return None
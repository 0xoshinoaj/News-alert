import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# 初始化 UserAgent
ua = UserAgent()

def get_page(url):
    headers = {
        'User-Agent': ua.random  # 隨機生成 User-Agent
    }
    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.text, 'html.parser')
from utils.http_utils import get_page
from utils.data_processing import extract_articles

def scrape(url, source):
    soup = get_page(url)
    return extract_articles(soup, source)
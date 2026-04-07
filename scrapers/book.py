import requests
from bs4 import BeautifulSoup
from config import HEADERS


def scrape_book(url):

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
    except:
        return {}

    soup = BeautifulSoup(response.text, "lxml")

    def safe(selector):
        el = soup.select_one(selector)
        return el.text.strip() if el else None

    book = {}

    book["title"] = safe("#productTitle")
    book["author"] = safe(".author a")
    book["rating"] = safe(".a-icon-alt")
    book["reviews"] = safe("#acrCustomerReviewText")
    book["price"] = safe(".a-price .a-offscreen")

    desc = soup.select_one("#bookDescription_feature_div")
    book["description"] = desc.text.strip() if desc else None

    return book
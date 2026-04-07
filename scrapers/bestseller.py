import requests
from bs4 import BeautifulSoup
from config import BESTSELLER_URL, HEADERS, BASE_URL

def get_bestseller_books():

    response = requests.get(BESTSELLER_URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, "lxml")

    books = []

    items = soup.select(".zg-grid-general-faceout")

    for item in items:

        rank = item.select_one(".zg-bdg-text")
        img = item.select_one("img")
        link = item.select_one("a")
        rating = item.select_one(".a-icon-alt")

        books.append({
            "rank": rank.text.replace("#", "").strip() if rank else None,
            "title": img["alt"] if img else None,
            "rating": rating.text if rating else None,
            "link": BASE_URL + link["href"] if link else None
        })

    return books
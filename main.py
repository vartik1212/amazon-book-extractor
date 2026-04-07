import time
from tqdm import tqdm

from scrapers.bestseller import get_bestseller_books
from scrapers.book import scrape_book
from storage.writer import save_books
from ai.theme_extractor import extract_themes
from config import REQUEST_DELAY


def run():

    print("Collecting bestseller books...")

    books = get_bestseller_books()

    dataset = []

    for book in tqdm(books):

        try:

            details = scrape_book(book["link"])

            details["themes"] = extract_themes(details["description"])

            dataset.append(details)

            time.sleep(REQUEST_DELAY)

        except Exception as e:
            print("Error:", e)

    save_books(dataset)


if __name__ == "__main__":
    run()
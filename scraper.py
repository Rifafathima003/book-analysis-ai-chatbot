import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

titles, prices, ratings, availability = [], [], [], []

session = requests.Session()

for page in range(1, 11):  # scrape 10 pages
    url = base_url.format(page)
    response = session.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.p["class"][1]
        avail = book.find("p", class_="instock availability").text.strip()

        titles.append(title)
        prices.append(price)
        ratings.append(rating)
        availability.append(avail)

df = pd.DataFrame({
    "Title": titles,
    "Price": prices,
    "Rating": ratings,
    "Availability": availability
})

df.to_csv("data/raw_books.csv", index=False)
print("✅ Scraping done!")
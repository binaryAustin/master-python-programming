import csv
import requests
from bs4 import BeautifulSoup

url = "https://xuepc.vn/mainboard-intel-z890"

res = requests.get(url, timeout=10.0)

soup = BeautifulSoup(res.content, "html.parser")

items = soup.find_all("div", class_="p-item")


with open("web_scraping/products.csv", mode="w", encoding="utf-8") as fw:
    writer = csv.writer(fw)
    writer.writerow(["id", "name", "price"])
    for index, item in enumerate(items):
        name: str = item.h3.text
        price = int(item.find("p", class_="p-price-sale").text.replace(".", "")[:-1])
        writer.writerow([index + 1, name, price])

import requests
import pandas as pd
from bs4 import BeautifulSoup

data = {'title': [], 'price': [], 'reviews': []}

url = "https://www.amazon.in/s?k=iphone+14&sprefix=ip%2Caps%2C211&ref=nb_sb_ss_ts-doa-p_1_2"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

try:
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
    prices = soup.select("span.a-price-whole")
    reviews = soup.select("span.a-size-base.s-underline-text")

    for span, price, review in zip(spans, prices, reviews):
        title = span.string
        product_price = price.get_text()
        product_review = review.get_text() if review else ""
        print(title, product_price, product_review)
        data["title"].append(title)
        data["price"].append(product_price)
        data["reviews"].append(product_review)

    df = pd.DataFrame.from_dict(data)
    df.to_csv("dataNew.csv", index=False)
    print("Data saved successfully!")
except Exception as e:
    print("An error occurred:", str(e))

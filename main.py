import smtplib

import requests as requests
from bs4 import BeautifulSoup
import lxml

PRODUCT_URL = "https://www.amazon.in/Apple-MacBook-Chip-13-inch-512GB/dp/B08N6DXX1V/ref=sr_1_3?keywords=macbook%2Bm1%2Bair%2B512%2Bgb&qid=1636604140&sr=8-3&th=1"
MY_EMAIL = {}
MY_PASSWORD = {}

headers = {
    # Enter computer's HTTP header.
}
response = requests.get(url=PRODUCT_URL, headers=headers)
page = response.text

soup = BeautifulSoup(page, "lxml")

price_tag = soup.find(name="span", class_="priceBlockBuyingPriceString")
product_name_tag = soup.find(name="span", class_="product-title-word-break")
product_name = product_name_tag.get_text().strip()

price = price_tag.get_text()
price_without_currency = price.split("₹")[1]
price_without_currency = price_without_currency.replace(",", "")
price_as_float = float(price_without_currency)

# print(price_as_float)
# print(product_name)

target_price_input = input(f"Enter the target price: ₹")

TARGET_PRICE = float(target_price_input)
ACTUAL_PRICE = price_as_float

if ACTUAL_PRICE <= TARGET_PRICE:

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Amazon Price Alert!\n\n{product_name} is now available at {price}.\nFollow the link to buy the product:\n{PRODUCT_URL}".encode('utf-8'))


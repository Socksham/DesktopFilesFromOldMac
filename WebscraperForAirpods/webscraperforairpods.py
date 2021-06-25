import math
import smtplib
import time

import requests
from bs4 import BeautifulSoup

converted_price = 0

cheapest_price = 300000000

prices_list = []

URLS = ['https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/dp/B07PXGQC1Q/ref=sr_1_3?keywords=airpods+2&qid=1574824161&sr=8-3', "https://www.walmart.com/ip/Apple-AirPods-with-Charging-Case-Latest-Model/604342441", "https://www.apple.com/shop/product/MV7N2/airpods-with-charging-case", "https://www.bestbuy.com/site/apple-airpods-with-charging-case-latest-model-white/6084400.p?skuId=6084400", "https://www.abt.com/product/133366/Apple-AirPods-With-Charging-Case-MV7N2AMA.html", "https://www.costco.com/CatalogSearch?dept=All&keyword=airpods"]

def check_price():
    global cheapest_price
    previous_price = cheapest_price
    for URL in URLS:
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
        
        page = requests.get(URL, headers=headers)

        soup = BeautifulSoup(page.content, 'html.parser')
        if URL == "https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/dp/B07PXGQC1Q/ref=sr_1_3?keywords=airpods+2&qid=1574824161&sr=8-3":
            price = soup.find(id="priceblock_ourprice").get_text()
        elif URL == "https://www.walmart.com/ip/Apple-AirPods-with-Charging-Case-Latest-Model/604342441":
            price = soup.find(id="price").get_text()
        elif URL == "https://www.apple.com/shop/product/MV7N2/airpods-with-charging-case":
            price = soup.find("span", {"class": "current_price"}).getText().strip()
        elif URL == "https://www.bestbuy.com/site/apple-airpods-with-charging-case-latest-model-white/6084400.p?skuId=6084400":
            price = soup.find("div", class_= "priceView-hero-price priceView-customer-price").find("span").getText()
        elif URL == "https://www.costco.com/CatalogSearch?dept=All&keyword=airpods":
            price = soup.find("div", id = "price-100487204").getText()
        converted_price = price[1:7]
        print(converted_price)
        prices_list.append(converted_price)

        cheapest_price = min(prices_list)
        if cheapest_price == converted_price:
            cheapest_price_url = URL


    print(cheapest_price_url, cheapest_price)
    send_mail(cheapest_price, cheapest_price_url)


def send_mail(price, URL):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    username = "webscraper.saksham@gmail.com"
    password = "varshney"

    server.login(username, password)
    price = str(price)
    price = "$" + price
    subject = "Price"
    link = URL

    msg = link

    server.sendmail(username, 'catchgsaksham@gmail.com', msg)

    print("EMAIL SENT")

    server.quit()

# while True:
#     check_price()
#     time.sleep(2)
check_price()
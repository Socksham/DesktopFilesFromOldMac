from bs4 import BeautifulSoup
import requests

# <span id="priceblock_ourprice" class="a-size-medium a-color-price priceBlockBuyingPriceString">$179.99</span>

URLS = ['https://www.amazon.com/Royalbaby-Space-Aluminum-Wheels-Orange/dp/B01N6QIUIK/ref=sr_1_2_sspa?keywords=bicycle&qid=1578689967&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVjRCRVBFSkRHWElLJmVuY3J5cHRlZElkPUEwMDEwODM3MkJMWVVWMk9UR1BONiZlbmNyeXB0ZWRBZElkPUEwMjU2NTc0WThSNU85WTQ4VU04JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==', "https://www.walmart.com/ip/Apple-AirPods-with-Charging-Case-Latest-Model/604342441", "https://www.apple.com/shop/product/MV7N2/airpods-with-charging-case", "https://www.bestbuy.com/site/apple-airpods-with-charging-case-latest-model-white/6084400.p?skuId=6084400", "https://www.costco.com/CatalogSearch?dept=All&keyword=airpods"]

def findPrice():
    for URL in URLS:

        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
        page = requests.get(URL, headers=headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        if URL == 'https://www.amazon.com/Royalbaby-Space-Aluminum-Wheels-Orange/dp/B01N6QIUIK/ref=sr_1_2_sspa?keywords=bicycle&qid=1578689967&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVjRCRVBFSkRHWElLJmVuY3J5cHRlZElkPUEwMDEwODM3MkJMWVVWMk9UR1BONiZlbmNyeXB0ZWRBZElkPUEwMjU2NTc0WThSNU85WTQ4VU04JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==':
            print("here")
            price = soup.find("div", class_ = "a-size-medium a-color-price priceBlockBuyingPriceString")

        elif URL == "https://www.walmart.com/ip/Apple-AirPods-with-Charging-Case-Latest-Model/604342441":
            price = soup.find(id="price").get_text()
        elif URL == "https://www.apple.com/shop/product/MV7N2/airpods-with-charging-case":
            price = soup.find("span", {"class": "current_price"}).getText().strip()
        elif URL == "https://www.bestbuy.com/site/apple-airpods-with-charging-case-latest-model-white/6084400.p?skuId=6084400":
            price = soup.find("div", class_= "priceView-hero-price priceView-customer-price").find("span").getText()
        elif URL == "https://www.costco.com/CatalogSearch?dept=All&keyword=airpods":
            price = soup.find("div", id = "price-100487204").getText()


        print(price)

findPrice()
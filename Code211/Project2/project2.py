import requests
from bs4 import BeautifulSoup

import smtplib

import re



email_to_send_to = None

#champs class ProductPrice
#footlocker class ProductPrice
#finishline class fullPrice

print("This webscraper looks for the cheapest price for a shoe of your liking.")
print(" ")
print("It then sends you an email for the cheapest price only when it finds a cheaper price")
print(" ")
print("To ensure that this process actually benefits you please look for the same shoe on all three websites and include the entire website(https//:...)")
print(" ")
champsURL = input("Please input a URL from champssports.com: ")
print(" ")
footlockerURL = input("Please input a URL from footlocker.com: ")
print(" ")
finishlineURL = input("Please input a URL from finishline.com: ")
print(" ")

# URLS = [champsURL, footlockerURL, finishlineURL]
URLS = [champsURL, footlockerURL, finishlineURL]

def check_price():
    prices = []
    converted_prices = []
    for URL in URLS:
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
        
        page = requests.get(URL, headers=headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        if URL == champsURL:
            price = soup.find("div", class_ = "ProductPrice").get_text()
        elif URL == footlockerURL:
            price = soup.find("div", class_ = "ProductPrice").get_text()
        elif URL == finishlineURL:
            price = soup.find("span", class_ = "fullPrice").get_text()
        prices.append(float(re.findall(r"[-+]?\d*\.\d+|\d+", price)[0]))
    cheapest_price = min(prices)

    send_mail(cheapest_price, URLS[prices.index(cheapest_price)])

def send_mail(price, URL):
    print(price, URL)
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
    email_to_send_to = input("What is your email: ")
    
    message = f"""\
    Cheapest Price Found!

    {price}\n{URL}"""
    server.sendmail(username, email_to_send_to, message)

    print("EMAIL SENT")

    server.quit()


check_price()

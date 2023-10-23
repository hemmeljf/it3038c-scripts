import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.reebok.com/p/100069897/bb-4000-ii-shoes")
soup = BeautifulSoup(response.text, 'html.parser')
name_span = soup.find("h1", {"class":"tag_h1_light--2sTWu  product-wrapper-title--1ky4m"})
title = name_span.text if name_span else "BB 4000 II Shoes"
price_span = soup.find("p", {"class":"tag_p--1xo5V product-price-regular--3cFbN false"})
price = price_span.text
print("Item %s has price %s" % (title, price))

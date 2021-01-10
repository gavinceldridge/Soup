from bs4 import BeautifulSoup
from selenium import webdriver
from send_twilio_text import send_text
import time

# print(soup.prettify())

while True:
        
    driver = webdriver.Chrome()
    url = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?acampID=0&cmp=RMX&irclickid=R00S%3Ac13txyLTHf0EHQlB1XYUkEy5hyBuV0M1o0&irgwc=1&loc=Narrativ&mpid=376373&ref=198&skuId=6439402"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    mydivs = soup.findAll("div", {"class": "add-to-cart-button"})

    print(mydivs)

    if mydivs != []:
        send_text('3060 IN STOCK!!!', '+18312772449')
    time.sleep(60)

# print(mydivs)

# from bs4 import BeautifulSoup
# import requests

# page = requests.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?acampID=0&cmp=RMX&irclickid=R00S%3Ac13txyLTHf0EHQlB1XYUkEy5hyBuV0M1o0&irgwc=1&loc=Narrativ&mpid=376373&ref=198&skuId=6439402")

# soup = BeautifulSoup(page.content, 'html.parser')

# pretty_soup = soup.prettify()

# print(pretty_soup)

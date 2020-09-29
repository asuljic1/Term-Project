import requests
from bs4 import BeautifulSoup


url = 'https://www.amazon.com/dp/B07XKF5RM3/ref=ods_gw_ha_btf_dash_lsr_092620?pf_rd_r=CE0CKRQTPKNBDY6XD9DG&pf_rd_p=b783eb6c-5da9-4fe3-9b0c-38a7927b0265'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}


# def check_price():
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
# converted_price = float(price[0:3])
converted_price = price

if (price < 100):
    print(converted_price)

print(title.strip())


# def send_mail():
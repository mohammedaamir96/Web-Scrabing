from bs4 import BeautifulSoup

import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
r = requests.get("https://www.zomato.com/bangalore/top-restaurants",headers=headers)

data=r.text

soup = BeautifulSoup(data,"html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))
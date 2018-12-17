from bs4 import BeautifulSoup
import requests

headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
r = requests.get("https://www.dominos.co.in/menu/chicken",headers=headers)
data=r.text
soup=BeautifulSoup(data,"html.parser")

products = soup.find_all("div",attrs={"class":"tab-content col-xs-12 pd-N"})
#print(products)

items = soup.find_all("div",attrs={"class":"col-xs-12 product-box our-menu-box"})
#print(items)

data = soup.find_all("div",attrs={"class":"row vertical-box displayFlex"})
#print(data)

list=items[0].select('h3')
#print(list)

for i in list:
    j=i.getText()
    print(j)

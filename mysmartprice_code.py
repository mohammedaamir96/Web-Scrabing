from bs4 import BeautifulSoup
import requests

headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
r = requests.get("https://www.mysmartprice.com/mobile/pricelist/mobile-price-list-in-india.html",headers=headers)
data=r.text
soup=BeautifulSoup(data,"html.parser")
a=[]
b=[]

products = soup.find_all("div",attrs={"class":"prdct-grid-wrpr js-prdct-grid-wrpr"})
#print(products)

items= soup.find_all("div",attrs={"class":"prdct-item__dtls"})
#print(items)

name= soup.find_all("a",attrs={"class":"prdct-item__name"})
#print(name)

prices=soup.find_all("div",attrs={"class":"prdct-item__prc main-wrpr__cols1"})
#print(prices)

for i in name:
    j=i.getText()
    a.append(j)
#print(a)
for k in prices:
    s=k.getText()
    b.append(s)
#print("\t",b)

for i,j in zip(a,b):
    print(i,"\n\t",j)
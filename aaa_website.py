import requests
from bs4 import BeautifulSoup
import re
import csv

#Used headers/agent because the request was timed out and asking for an agent.
#Using following code we can fake the agent.
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
zipcode=str(input("enter zipcode:"))
response = requests.get("https://www.aaa.com/autorepair/locations/"+zipcode+"?radius=50&itemcategory=&napalocations",headers=headers)

content = response.content
soup = BeautifulSoup(content,"html.parser")
a=[]
b=[]
c=[]
d=[]
data=soup.find_all("div",attrs={"class":"aaa-inline-blockContainer"})
#print(data)

data1 = soup.find_all("div", attrs={"class": "aar-detail-wrapper"})
#print(data1)

name=soup.find_all("span",class_="b3 regularText aar-title dl-item-name")
#print(name)

for i in name:
    j=i.getText()
    a.append(j)

address=soup.find_all("span",attrs={"class":"blk5 regularText aar-address1"})
#print(address)

for i in address:
    j=i.getText()
    b.append(j)

address1=soup.find_all("span",attrs={"class":"blk5 regularText aar-address2"})
#print(address1)

for i in address1:
    j=i.getText().replace(" ","").replace("\n","").replace(","," ")
    c.append(j)

miles=soup.find_all("span",attrs={"class":"blk3 aaa-miles"})
#print(miles)

for i in miles:
    j=i.getText().__add__(" miles")
    d.append(j)
#print(d)
with open("C:/Users/Aamir/Desktop/aamir.csv",mode='w',newline="") as aa:
    ab=csv.writer(aa,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
    ab.writerow(['company name','address','distance'])
    for (i, j, k, l) in zip(a,b,c,d):
        ab.writerow([i,j+k,l])
    print("success")


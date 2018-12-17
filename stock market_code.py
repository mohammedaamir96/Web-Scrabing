import requests
from bs4 import BeautifulSoup
import re

#Used headers/agent because the request was timed out and asking for an agent.
#Using following code we can fake the agent.
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
response = requests.get("https://www.moneycontrol.com/stocks/marketstats/sector-scan/bse/today.html",headers=headers)

content = response.content
soup = BeautifulSoup(content,"html.parser")

pro = soup.find_all("div",attrs={"class":"acrcbx"})
#print(pro)

dat = soup.find_all("div",attrs={"class":"accrMain"})
#print(dat)

for i in dat:
    j=i.text
    print(j)

with open("C:/Users/Aamir/Desktop/aa.csv",mode='w',newline="") as ab:
    ac=csv.writer(ab,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
    ac.writerow(["sector","market-cap","chg","ratio","advance","decline"])
    for i in dat:
        ac.writerow(i)
    print("success")

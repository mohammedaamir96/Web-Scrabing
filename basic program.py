from bs4 import BeautifulSoup

import requests

##url = input("Enter a website to extract the URL's from: ")

r  = requests.get("https://pythonforbeginners.com")

data = r.text

#print(data)

soup = BeautifulSoup(data,"html.parser")

#print(soup.find_all('a'))

'''for link in soup.find_all('a'):
    print(link)'''

for link in soup.find_all('a'):
    print(link.get('href'))
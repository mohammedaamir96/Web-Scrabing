import requests
from bs4 import BeautifulSoup
import re

#Used headers/agent because the request was timed out and asking for an agent.
#Using following code we can fake the agent.
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
response = requests.get("https://www.amazon.in/b/ref=s9_acss_bw_cg_Normaltv_8c1_w?node=12045104031&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=6NA68MJWYV5RYYEGB26K&pf_rd_t=101&pf_rd_p=3f9ba84c-d6ed-4177-8179-526be4456078&pf_rd_i=1389396031",headers=headers)

content = response.content
soup = BeautifulSoup(content,"html.parser")
a=[]

products = soup.find_all("div",attrs={"class":"a-row a-spacing-none"})
#print(products)

for i in products:
    j= i.text
    print(j)
import requests
from bs4 import BeautifulSoup
url = "https://movie.douban.com/top250"
headers = {"User-Agent":"Mozilla/5.0(Windows NT 10.0;Win64; x64)"}
response =requests.get(url,headers=headers,timeout=15)
print("状态码:",response.status_code)
soup = BeautifulSoup(response.text,"html.parser")
items = soup.find_all("div",class_="item")
print("找到",len(items),"部电影")
for it in items:
    title =it.find("span",class_="title").text
    score =it.find("span",class_="rating_num").text
    print(title,score)

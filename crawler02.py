import requests, time
from bs4 import BeautifulSoup
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
rank = 1
for start in range(0, 250, 25):
    url = "https://movie.douban.com/top250?start=" + str(start)
    response = requests.get(url, headers=headers, timeout=15)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all("div", class_="item")
    for it in items:
        title = it.find("span", class_="title").text
        score = it.find("span", class_="rating_num").text
        print(rank, title, score)
        rank = rank + 1
    time.sleep(0.5)
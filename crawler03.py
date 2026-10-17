import requests, time, csv
from bs4 import BeautifulSoup
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
rows = []          # 准备一个空列表，专门装数据
rank = 1
for start in range(0, 250, 25):
    url = "https://movie.douban.com/top250?start=" + str(start)
    response = requests.get(url, headers=headers, timeout=15)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all("div", class_="item")
    for it in items:
        title = it.find("span", class_="title").text
        score = it.find("span", class_="rating_num").text
        rows.append([rank, title, score])     # 攒起来，这次不打印
        rank = rank + 1
    time.sleep(0.5)
# 十页全抓完，最后一次性写进文件
with open("douban_top250.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["排名", "电影名", "评分"])   # 第一行：表头
    writer.writerows(rows)                      # 后面 250 行：数据
print("已保存", len(rows), "条到 douban_top250.csv")
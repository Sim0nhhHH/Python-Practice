# Python 练习仓库

我自学 Python 的练习代码，按天记录。包含基础语法练习、几个小工具，以及一个豆瓣电影 Top250 爬虫。

## 目录结构

| 文件 | 内容 |
|---|---|
| `day01.py` – `day13.py` | 每日练习（编号不连续，缺的是那天没写） |
| `grade.py` | 成绩等级判断 |
| `temp.py` | 摄氏 / 华氏温度互转 |
| `stat.py` | 成绩统计：平均分、最高分、最低分、等级分布 |
| `crawler01.py` | 豆瓣 Top250 爬虫 · 第一版：只抓第一页 25 部 |
| `crawler02.py` | 第二版：翻页循环，抓全部 250 部 |
| `crawler03.py` | 第三版：抓完存成 CSV |

## 怎么跑

需要 Python 3.13 或更高版本。

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

然后挑一个跑：

```powershell
python crawler03.py    # 爬豆瓣 Top250，生成 douban_top250.csv
python crawler02.py    # 只在屏幕上打印 250 部
```

## 说明

`day12.py` / `stat.py` 需要自备 `scores.txt`（一行一个分数），仓库里未提供。

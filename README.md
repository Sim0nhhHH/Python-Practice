# Python 练习仓库

我自学 Python 的练习代码，按天记录。包含基础语法练习、几个小工具，以及一个豆瓣电影 Top250 爬虫。

## 目录结构

| 文件 | 内容 |
|---|---|
| `day01.py` – `day13.py` | 每日练习（编号不连续，缺的是那天没写） |
| `grade.py` | 成绩等级判断 |
| `temp.py` | 摄氏 / 华氏温度互转 |
| `stat.py` | 成绩统计：平均分、最高分、最低分、等级分布 |
| `scores.txt` | 示例成绩数据（一行一个分数），`stat.py` 和 `day12.py` 读它 |
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
python stat.py         # 成绩统计
python crawler03.py    # 爬豆瓣 Top250，生成 douban_top250.csv
```

## 说明

`crawler*.py` 依赖豆瓣的公开页面，网站结构变化时可能失效。
爬虫已加入 `time.sleep(1)` 限速；生成的 CSV 不纳入版本控制。
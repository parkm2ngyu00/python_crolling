from wsgiref.util import request_uri
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=183559&weekday=mon"
res = requests.get(url)
res.raise_for_status

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("td", attrs={"class": "title"})

# 만화 제목 + 링크 가져오기
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    print(title, link)

# 평점 구하기
cartoons = soup.find_all("div", attrs={"class": "rating_type"})
totalrate = 0
i = 0
for cartoon in cartoons:
    rate = float(cartoon.strong.get_text())
    i += 1
    totalrate += rate

print(totalrate / i)

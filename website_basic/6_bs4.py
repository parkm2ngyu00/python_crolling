from wsgiref.util import request_uri
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)  # soup 객체에서 처음 발견되는 a element 출력
# print(soup.a.attrs)  # a element 의 속성 정보를 출력
# print(soup.a.attrs["href"])  # a element 의 href 속성 '값' 정보를 출력

# class="" 인 a element 를 찾아줘
# print(soup.find("a", attrs={"class": "Nbtn_upload"}))
# class="" 인 element 를 찾아줘
# print(soup.find(attrs={"class": "Nbtn_upload"}))

# print(soup.find("li", attrs={"class": "rank01"}))
# rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2)
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="독립일기-11화 밥공기 딜레마")
print(webtoon)
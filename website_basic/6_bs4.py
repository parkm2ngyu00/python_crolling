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
# # class="" 인 element 를 찾아줘
# print(soup.find(attrs={"class": "Nbtn_upload"}))

# print(soup.find("li", attrs={"class": "rank01"}))
rank1 = soup.find("li", attrs={"class": "rank01"})
print(rank1.a)

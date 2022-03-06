import requests
from bs4 import BeautifulSoup

url = "https://realty.daum.net/home/apt/danjis/38487/items?business=da_www&mkt_source=&service_type=%EC%9E%85%EC%A3%BC2%EB%85%84%ED%9B%84"
res = requests.get(url)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

with open("quiz.html", "w", encoding="utf8") as f :
    f.write(soup.prettify())
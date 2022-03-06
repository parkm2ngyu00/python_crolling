from optparse import Option
from attr import attrs
from selenium  import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome("C:\Downloads\chromedriver_win32\chromedriver.exe", options=options)
browser.maximize_window()

url = "https://play.google.com/store/movies"
browser.get(url)

# 화면 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True :
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height :
        break
    prev_height = curr_height
    
print("스크롤 완료")

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

# movies = soup.find_all("a", attrs={"class" : ["Si6A0c itIJzb", "Vpfmgd"]})
movies = soup.find_all("a", attrs={"class" : "Vpfmgd"})
for movie in movies :
    title = movie.find("div", attrs = {"class" : "WsMG1c nnK0zc"}).get_text()

    # 할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price :
        original_price = original_price.get_text()
    else :
        # print("title", "   <할인되지 않은 영화 제외>")
        continue
    
    # 할인 된 가격
    price = movie.find("span", attrs={"class":"vdioaD asdie2 aASDcv"}).get_text()

    # 링크
    link = movie.find("a", attrs={"class":"Sdvbv"})["href"]

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://google.com/store/movies" + link)
    print("-" * 100)

browser.quit()
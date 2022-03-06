from distutils.errors import LinkError
import requests
from bs4 import BeautifulSoup
import re

hearders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}

for i in range(1, 6) : 

    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor=".format(i)
    res = requests.get(url, headers=hearders)
    res.raise_for_status
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class": re.compile("^search-product")})
    # print(items[0].find("div", attrs={"class": "name"}).get_text())

    for item in items:
        # print("페이지 : ", i)
        # 광고 제품은 제외
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge :
            # print("<광고 상품 제외합니다>")
            continue

        name = item.find("div", attrs={"class": "name"}).get_text()

        # 애플 제품 제외
        if "Apple" in name :
            # print("애플 상품 제외합니다.")
            continue

        price = item.find("strong", attrs={"class": "price-value"}).get_text()
        rate = item.find("em", attrs={"class": "rating"})
        rate_count = item.find("span", attrs={"class": "rating-total-count"})

        if rate and rate_count :
            rate = rate.get_text()
            rate_count = rate_count.get_text()
            rate_count = rate_count[1 : -1]
        else :
            # print("<평점 없는 상품 제외합니다.>")
            continue
        
        link = item.find("a", attrs={"class" : "search-product-link"})["href"]

        # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
        if float(rate) >= 4.5 and int(rate_count) >= 100: 
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate} ({rate_count})")
            print("바로가기 : {}".format("https://www.coupang.com" + link))
            print("-" * 100)
        else :
            continue
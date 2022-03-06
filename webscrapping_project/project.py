import requests
from bs4 import BeautifulSoup
import re


# [오늘의 날씨]
# 흐림, 어제보다 00높아요
# 현재 00 (최저 00 / 최고 00)
# 강수확률 00%

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
res = requests.get(url)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

curr_tem = soup.find("div", attrs={"class":"temperature_text"}).find("strong").get_text()
summary = soup.find("div", attrs={"class":"temperature_info"}).find("p").get_text()
summary_info = soup.find("div", attrs={"class":"temperature_info"}).find("dl").get_text().strip()
items = soup.find_all("li", attrs={"class":"item_today level1"})
print("[오늘의 날씨]")
print(curr_tem)
print(summary)
print(summary_info)
print(items[0].get_text().strip() + ",", items[1].get_text().strip() + ",", items[2].get_text().strip())

# [IT 뉴스]
# 1. 무슨 무슨 일이...
#  (링크 : https://...)
# 2. 무슨 무슨 일이...
#  (링크 : https://...)
# 3. 무슨 무슨 일이...
#  (링크 : https://...)

url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

cluster = soup.find_all("li", attrs={"class":"cluster_item"}, limit=3)
for idx, head_news in enumerate(cluster) :
    news = head_news.find("div", attrs={"class":"cluster_text"}).a.get_text()
    news_link = head_news.find("div", attrs={"class":"cluster_text"}).a["href"]
    print(str(idx + 1) + ".", news)
    print(news_link)
    # if idx >= 2 :
    #     break

# 매일 영어 회화 학습
# [오늘의 영어 회화]
# (영어 지문)
# ...
# (한글 지문)
# ...

url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

text = soup.find_all("div", attrs={"class":"conv_txtBox"})
kor_texts = text[0].find_all("div", attrs={"id":re.compile("^conv_kor_t")})
eng_texts = text[1].find_all("div", attrs={"id":re.compile("^conv_kor_t")})

print("[오늘의 영어 회화]")
print("(한글 지문)")

for kor_text in kor_texts :
    kor_text = kor_text.span.b.get_text()
    print(kor_text)

print("(영어 지문)")

for eng_text in eng_texts :
    eng_text = eng_text.span.b.get_text()
    print(eng_text)
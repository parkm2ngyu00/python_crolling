from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome("C:\Downloads\chromedriver_win32\chromedriver.exe")
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"
browser.get(url)

# try:
#     element = WebDriverWait(browser, 5).until(
#         EC.presence_of_element_located((By.LINK_TEXT , '도착'))
#     )
# finally:
#     browser.quit()

browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()
time.sleep(2)
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[3]/td[4]/button").click()
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[3]/td[5]/button").click()
browser.find_elements_by_link_text("7")[0].click()
browser.find_elements_by_link_text("8")[0].click()


# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[6]/div/div[2]/div/ul/li[1]/button/figure/img").click()
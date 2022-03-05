from selenium import webdriver
browser = webdriver.Chrome("C:\Downloads\chromedriver_win32\chromedriver.exe")
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"
browser.get(url)


browser.find_element_by_link_text("가는 날").click()
browser.find_elements_by_link_text("27")[0].click()
browser.find_elements_by_link_text("28")[0].click()

browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[6]/div/div[2]/div/ul/li[1]/button/figure/img").click()
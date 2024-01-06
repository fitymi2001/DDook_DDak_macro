from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome() # 웹 드라이버 열기
url = 'https://google.com'
driver.get(url) # url 링크 크롬으로 열기
driver.maximize_window() # 전체화면으로 열기
action = ActionChains(driver) # 액션 변수를 통해서 driver를 제어

# XPath를 사용하여 버튼 클릭
xpath_button = driver.find_element(By.XPATH, "//*[@id='gb']/div/div[2]/a")
xpath_button.click()

# 프로그램 종료를 방지하기 위해 일정 시간 대기

# 필요에 따라 아래 코드를 사용하여 사용자가 직접 브라우저를 닫을 때까지 대기
# input("Press Enter to close the WebDriver...")  # 사용자가 Enter를 누를 때까지 대기
# driver.quit()  # WebDriver 종료
#//*[@id="gb"]/div/div[2]/a
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

wd.get("https://tradingeconomics.com/calendar")
wd.maximize_window()
assert "Economic Calendar" in wd.title

countries=wd.find_elements(By.XPATH,'//table[@id="calendar"]/tbody/tr/td[2]')
event=wd.find_elements(By.XPATH,'//table[@id="calendar"]/tbody/tr/td[3]' )
actual=wd.find_elements(By.XPATH,'//table[@id="calendar"]/tbody/tr/td[4]' )
previous=wd.find_elements(By.XPATH,'//table[@id="calendar"]/tbody/tr/td[5]' )
concensus=wd.find_elements(By.XPATH,'//table[@id="calendar"]/tbody/tr/td[6]' )

for c in actual:
   print(c.text)
# print(str(len(countries)) + str(countries[1]))
# print(str(len(event)) + str(event[1]))
# print(str(len(actual)) + str(actual[1]))
# print(str(len(previous)) + str(previous[1]))
# print(str(len(concensus)) + str(concensus[1]))
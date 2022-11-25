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
assert "Economic Calendar" in wd.title

# Make Python sleep for some time#sleep(2)


time.sleep(2)
for table in wd.find_elements('//*[contains(@id,"eventHistoryTable")]//tr'):
    data = [item.text for item in table.find_elements(".//*[self::td or self::th]")]
    print(data)
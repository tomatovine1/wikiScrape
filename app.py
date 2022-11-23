
# Importing Libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import re

# Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Creating WebDriver instance
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

wd.get("https://www.wikipedia.org/")
assert "Wikipedia" in wd.title
# print(wd.page_source)

input_element = wd.find_element(by=By.ID, value="searchInput")
input_element.send_keys("ASD")
search = wd.find_element(by=By.CLASS_NAME, value="pure-button")
search.click()

window_after = wd.window_handles[0]
wd.switch_to.window(window_after)

assert "ASD - Wikipedia" in wd.title
print ("Successfully loaded the page", wd.title)

link_text = wd.find_element(By.LINK_TEXT, "Adaptive software development")
link_text.click()

window_after = wd.window_handles[0]
wd.switch_to.window(window_after)

assert "Adaptive software development - Wikipedia" in wd.title
print ("Successfully loaded the page", wd.title)

p_tags = wd.find_elements(by=By.TAG_NAME, value="p")
print("Number of tags found: ", len(p_tags))

info_lines = ''

for p_tag in p_tags:
    info_lines += p_tag.text
    info_lines += "\n"
#print(info_lines)

# Match all digits occurring in squared brackets in the string and replace them with an empty string
pattern = r'\[[0-9]\]'
new_string = re.sub(pattern, '', info_lines)
print(new_string)

elems = wd.find_elements(by=By.CSS_SELECTOR, value='p > a')
dict_links = {}
for e in elems:
    dict_links[e.text] = e.get_attribute('href')
print(dict_links)

print(" OK ____------")
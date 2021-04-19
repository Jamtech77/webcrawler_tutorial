from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# --> 自動アクセスを実装してみる
options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(options=options)
url = 'https://search.yahoo.co.jp/image'
driver.get(url)

sleep(2)

query = 'Programming'
search_box = driver.find_element_by_class_name('SearchBox__searchInput')
search_box.send_keys(query)
search_box.submit()

sleep(3)
driver.quit()

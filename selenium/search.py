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

height = 1000
# Execute Javascript
# driver.execute_script("window.scrollTo(x, y)")  
while height < 10000:
    driver.execute_script("window.scrollTo(0, {})".format(height))  
    height += 100
    sleep(1)

sleep(2)
driver.quit()

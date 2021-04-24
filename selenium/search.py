from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd


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
while height < 2000:
    driver.execute_script("window.scrollTo(0, {})".format(height))  
    height += 100
    sleep(1)

# Get elements of images
elements = driver.find_elements_by_class_name('sw-Thumbnail')

d_list = []
# Get URL from elements
for i, element in enumerate(elements, start=1):
    name = f'{query}_{i}'
    yahoo_image_url = element.find_element_by_tag_name('img').get_attribute('src')
    raw_url = element.find_element_by_class_name('sw-ThumbnailGrid__details').get_attribute('href')
    title = element.find_element_by_tag_name('img').get_attribute('alt')

    d = {
        'filename': name,
        'raw_url': raw_url,
        'yahoo_image_url': yahoo_image_url,
        'title': title
    }

    d_list.append(d)

    sleep(2)

df = pd.DataFrame(d_list)
df.to_csv('image_urls.csv')

sleep(2)
driver.quit()

import requests
from bs4 import BeautifulSoup

url = "https://search.books.com.tw/search/query/key/python/cat/all"
result = requests.get(url, timeout=5) # 對server發送request
# print(result) # Get responds means that we get responds from server.
html = result.text
soup = BeautifulSoup(html, 'html.parser') # 解析html
print(soup.title)   # 此title為網頁的標題


def parse(items):
    for node in items:
        #print(node.h3.a.text)  # 印出內容文字
        print(node.h3.a.text.strip())   # strip()是將空格去除


books_items = soup.find_all('li', class_='item')    # 由於class會是特定字，這裡才被加了底線

parse(books_items)


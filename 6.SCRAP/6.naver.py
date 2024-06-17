import requests
from bs4 import BeautifulSoup

url = 'https://sports.news.naver.com/index'

data = requests.get(url)

soup = BeautifulSoup(data.text, 'html.parser')

# 신문기사 제목 및 링크 출력

# today_item_li = soup.select_one('.today_item')
# # print(today_item_li)

# for today_new_name in today_item_li:
#     news_name = today_new_name.text

# news_name = today_item_li.select('strong')
# print(news_name)

news_list = soup.select('.today_list > li')
# print(len(news_list))

for news in news_list:
    a_tag = news.select_one('a')
    print(a_tag['title'])
    print(a_tag['href'])
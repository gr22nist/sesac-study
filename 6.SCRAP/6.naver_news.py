import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/section/105'

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

headlines = soup.select('li.sa_item._SECTION_HEADLINE')
# print(len(headlines))

for news in headlines:
    strong_tag = news.select_one('.sa_text_strong').text
    link_tag = news.select_one('.sa_text_title')
    # print(strong_tag)
    
    print(f"헤드라인 제목: {strong_tag}")
    print(f"링크: {link_tag['href']}")

print('-' * 80)

news_list = soup.select('li.sa_item._LAZY_LOADING_WRAP')
# print(len(news_list))

for news in news_list:
    strong_tag = news.select_one('.sa_text_strong').text
    link_tag = news.select_one('.sa_text_title')
    # print(strong_tag)
    
    print(f"뉴스 제목: {strong_tag}")
    print(f"링크: {link_tag['href']}")
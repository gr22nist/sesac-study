import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/section/105'

data = requests.get(url)

soup = BeautifulSoup(data.text, 'html.parser')


headline_list = soup.select('.sa_list')
print(len(headline_list))

for news in headline_list:
    a_tag = news.select_one('a')
    print(a_tag['title'])
    print(a_tag['href'])
import requests
from bs4 import BeautifulSoup

# url = 'https://news.naver.com/section/105'


# data = requests.get(url)

# soup = BeautifulSoup(data.text, 'html.parser')

# # 헤드라인 뉴스와 일반 뉴스 제목/링크 뽑아오기


# news_list = soup.select('.today_list > li')
# # print(len(news_list))

# for news in news_list:
#     a_tag = news.select_one('a')
#     print(a_tag['title'])
#     print(a_tag['href'])

# base_url = 'https://search.naver.com/search.naver'
base_url = 'https://www.google.co.kr/search'

def naver_search(query):
    params = {'query': query}
    
    response = requests.get(base_url, params=params)
    return response.text

query = []
    
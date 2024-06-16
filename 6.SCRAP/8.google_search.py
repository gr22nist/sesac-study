import requests
from bs4 import BeautifulSoup

base_url = "https://www.google.co.kr/search"

def naver_search(query):
    params = {"q": query}

    response = requests.get(base_url, params=params, headers={"User-Agent": "Mozilla/5.0"})
    return response.text

query = "파이썬 프로그래밍"
contents = naver_search(query)

soup = BeautifulSoup(contents, 'html.parser')

search_result = soup.select('div.g')

for item in search_result:
    title_tag = item.select_one('div.yuRUbf > a > h3')
    link_tag = item.select_one('div.yuRUbf > a')
    content_tag = item.select_one('div.VwiC3b > span')
    
    if title_tag and link_tag and content_tag:
        title = title_tag.get_text()
        link = link_tag['href']
        content = content_tag.get_text()
        
        print(f"제목: {title}")
        print(f"링크: {link}")
        print(f"내용: {content}")
        print()
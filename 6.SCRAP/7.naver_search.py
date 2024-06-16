import requests
from bs4 import BeautifulSoup

base_url = "https://search.naver.com/search.naver"

def naver_search(query):
    params = {"query": query}

    response = requests.get(base_url, params=params, headers={"User-Agent": "Mozilla/5.0"})
    return response.text

query = "파이썬 프로그래밍"
contents = naver_search(query)

soup = BeautifulSoup(contents, 'html.parser')

search_result = soup.select('div.api_ani_send')

for item in search_result:
    title_tag = item.select_one('a.api_txt_lines')
    link_tag = item.select_one('a.api_txt_lines')
    content_tag = item.select_one('div.api_txt_lines.dsc_txt')
    
    if title_tag and link_tag and content_tag:
        title = title_tag.get_text()
        link = link_tag['href']
        content = content_tag.get_text()
        
        print(f"제목: {title}")
        print(f"링크: {link}")
        print(f"내용: {content}")
        print()
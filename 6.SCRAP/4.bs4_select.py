from bs4 import BeautifulSoup
import requests


html_doc = """
    <html>
    <head>
        <title>간단한 HTML 예제</title>
    </head>
    <body>
    <div class="container">
        <h1>안녕하세요</h1>
        <p>이것은 간단한 HTML 예제 입니다.</p>
        <p>이것은 간단한 HTML22 예제 입니다.</p>
    </div>
    <a href="https://www.naver.com"></a>
    <img src="example.jpg" alt="예제 이미지">
    <img src="example2.jpg" alt="예제 이미지2" width="500" height="600">
    <div class="content">
        <ul>
            <li>항목1</li>
            <li>항목2</li>
            <li>항목3</li>
        </ul>
    </div>
    <div id="footer">
        <p>Copyuright C <b>2024.</b> 이 <i>페이지</i>는 내꺼</p>
    </div>
    </body>
    </html>
"""

html_doc = requests.get('https://www.naver.com').text

soup = BeautifulSoup(html_doc, 'html.parser') # html.parser, lxml



link_tag = soup.select('a')
print(link_tag)

all_imgs = soup.select('img')
print(all_imgs)
for img in all_imgs:
    print(img['src'])
    
content_div = soup.select_one('div.content')
print(content_div)

footer_div = soup.select_one('div#footer')
print(footer_div)

li_lists = soup.select('div.content li')
print(li_lists)

li_lists = soup.find_all('div.content li')
print(li_lists) # find 시리즈는 태그명으로 검색하는 것

p_tag_div_footer = soup.select_one('div#footer')
b_text = p_tag_div_footer.select_one('b')
i_text = p_tag_div_footer.select_one('i')

print(f"볼드 텍스트: {b_text}, 이탤릭 텍스트: {i_text}")
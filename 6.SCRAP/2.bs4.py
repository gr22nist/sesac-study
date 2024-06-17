from bs4 import BeautifulSoup

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
        <p>Copyuright C 2024. 이 페이지는 내꺼</p>
    </div>
    </body>
    </html>
"""

soup = BeautifulSoup(html_doc, 'html.parser') # html.parser, lxml
# print(html_doc)
# print(soup)
# print(soup.head)
# print(soup.body.h1)
# print(soup.body.p)
# print(soup.p.text)

list_items = soup.ul.find_all('li')
# print(list_items)

# for li in list_items:
#     print(li.text)
# print(list_items[1].text)

# container_div = soup.find('div', class_='container')
# print(container_div.p.text)

# footer_div = soup.find('div', id='footer')
# print(footer_div.p.text)

# content_ul = soup.find('div', class_='content').ul
# print(content_ul)

# for li in content_ul.find_all('li'):
#     print(li.text)

link_tag = soup.a
print(link_tag.text)
naver_link = link_tag["href"]
print(link_tag["href"])

import requests

# response = requests.get(naver_link)
# print(response.text)

img_tag = soup.img
print(img_tag["src"])
print(img_tag["alt"])

img_tag = soup.find_all('img')
img_tag1 = img_tag[0]
img_tag2 = img_tag[1]
print(f'이미지태그1: ', img_tag1)
print(f'이미지태그2: ', img_tag2)


print(f'소스: {img_tag("src")}, ALT글자: {img_tag("alt")}, width: {img_tag.get("width"), "없음"}')
print(f'소스: {img_tag("src")}, ALT글자: {img_tag("alt")}, width: {img_tag2("width")}')

=======
# pip install bs4      # DOM을 파싱 (beautifulSoup4)

from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
    <title>간단한 HTML 예제</title>
</head>
<body>
    <h1>안녕하세요</h1>
    <p>이것은 간단한 HTML 예제입니다.</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser') # html.parser, lxml
print(html_doc)
print(soup)
# print(html_doc.head)  # 오류
print(soup.head)
print(soup.body.h1.text)
print(soup.p.text) # body 밖에 있는 모든 p까지
>>>>>>> feaeb15c487e35ece188ad2afe69aa9c6618c196

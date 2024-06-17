import requests
from bs4 import BeautifulSoup

url = 'https://www.pythonscraping.com/pages/page3.html'

data = requests.get(url)

soup = BeautifulSoup(data.text, 'html.parser')

# 여기에서 상품명과 가격을 출력하시오
# 개발자도구 사용으로 소스 참조로 정보 확인하기

# table_tag = soup.find('table', id='giftList')
# print(table_tag)


# table_tag = soup.select('#giftList')[0]
table_tag = soup.select_one('#giftList')
# table_tag = soup.select_one('table#giftList')
# print(table_tag)

product_trs = table_tag.select('tr')
print(product_trs)

item_list = []

for product_tr in product_trs[1:]:
    product_tds = product_tr.select('td')
    # print(product_tds[0], product_tds[2])
    item_list.append((product_tds[0].text.strip(),product_tds[2].text.strip()))


for item in item_list:
    print(f"상품명: {item_list[0]}, 가격: {item_list[1]}")


# name_tag = soup.select('tr.gift td')
# name_tag_text = name_tag[0].text
# print(name_tag)

# price_tag = soup.select_one('tr.gift td')[2].text
# print(price_tag)
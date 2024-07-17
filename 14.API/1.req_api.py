import requests

# 특정 사용자의 정보 조회하기
user_id = 1
url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"

response = requests.get(url)

post_data = response.json()

for comment in post_data:
    # print(comment)
    print(comment['title'])


# 2. 게시글 아이디 기준으로 댓글 가져오기

post_id = 1
url = f"https://jsonplaceholder.typicode.com/posts/{user_id}/comments"

response = response.get(url)
post_data = response.json()
for comment in post_data:
    print(comment['email'])
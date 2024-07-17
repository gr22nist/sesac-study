from my_jsonholder_api import JSONPlaceHolderAPI

# 해당 클래스 초기화
api = JSONPlaceHolderAPI()

user_posts = api.get_posts_by_user(1)

for comment in user_posts:
    print(comment['title'])
    
post_comments = api.get_comments_by_post(1)
for comment in post_comments:
    print(comment['title'])
    
def create_post(self, user_id, title, body):
    print('a')
    pass




# https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=c30b722a5623118f7b0cf9a350405ceb
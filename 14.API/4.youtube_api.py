import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('YOUTUBE_API_KEY')
url = 'https://www.googleapis.com/youtube/v3/search'

search_query = '최강야구'
params = {
    'part': 'snippet',
    'q': search_query,
    'type': 'video',
    'maxResults': 10,
    'key': API_KEY
}

response = requests.get(url, params=params)
response.raise_for_status()

data = response.json()
# print(data)

for item in data['items']:
    title = item['snippet']['title']
    video_id = item['id']['videoId']
    video_url = f'https://www.youtube.com/watch?v={video_id}'
    description = item['snippet']['description']
    
    print(f'영상 제목: {title}')
    # print(f'영상 아이디: {video_id}')
    print(f'영상 주소: {video_url}')
    print(f'영상 설명: {description}')
    print()
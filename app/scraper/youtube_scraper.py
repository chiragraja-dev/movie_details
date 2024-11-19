import json
from datetime import datetime
import os
from googleapiclient.discovery import build
import requests
from dotenv import dotenv_values,load_dotenv

load_dotenv()
API_KEY = os.getenv('YOUTUBE_API_KEY')
YOUTUBE_BASE_URL = 'https://www.googleapis.com/youtube/v3'

def get_comments(video_id, max_comments=2000):
    comments = []
    url = f"{YOUTUBE_BASE_URL}/commentThreads"
    params = {
        'part': 'snippet',
        'videoId': video_id,
        'key': API_KEY,
        'maxResults': 100
    }

    while len(comments) < max_comments:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print("Error:", response.json())
            break
        
        data = response.json()

        for item in data['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            comments.append({
                "textDisplay": comment['textDisplay'],
                "likeCount": comment['likeCount'],
                "publishedAt": comment['publishedAt']
            })

            if len(comments) >= max_comments:
                break

        if 'nextPageToken' in data:
            params['pageToken'] = data['nextPageToken']
        else:
            break

    return comments[:max_comments]


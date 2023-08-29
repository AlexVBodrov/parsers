import requests
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%d-%m-%Y %H_%M")

url = "https://www.youtube.com/embed/hN2eP8EuJm4"
response = requests.get(url=url, stream=True)

with open(f'exercise_3/{current_time}_file.mp4', 'wb') as video:
    for piece in response.iter_content(chunk_size=100000):
        video.write(piece)
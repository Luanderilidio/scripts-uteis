from yt_dlp import YoutubeDL
import os

def download_audio(video_url, output_folder='downloads'):
    os.makedirs(output_folder, exist_ok=True)
    options = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with YoutubeDL(options) as ydl:
        ydl.download([video_url])

# URL do vídeo ou playlist para baixar
video_url = "https://www.youtube.com/watch?v=ajnqTbVgVqI&list=PLq2aS32V3IdblMafYONv3Q59is2a4pgWC&index=1"

try:
    print(f"Baixando: {video_url}")
    download_audio(video_url)
    print(f"Download concluído: {video_url}")
except Exception as e:
    print(f"Erro ao baixar {video_url}: {e}")

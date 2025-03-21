import os
import subprocess

def get_video_duration(video_path):
    """
    Obtém a duração do vídeo em segundos usando FFmpeg.
    """
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "format=duration", "-of", "csv=p=0", video_path],
            capture_output=True, text=True, check=True
        )
        return float(result.stdout.strip())
    except Exception as e:
        print(f"Erro ao obter duração do vídeo {video_path}: {e}")
        return None

def delete_short_videos(folder_path, min_duration=6):
    """
    Percorre uma pasta e apaga os vídeos que forem menores que min_duration segundos.
    """
    if not os.path.exists(folder_path):
        print(f"A pasta {folder_path} não existe!")
        return
    
    video_extensions = ('.mp4', '.avi', '.mov', '.mkv', '.webm')
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path) and filename.lower().endswith(video_extensions):
            duration = get_video_duration(file_path)
            if duration is not None and duration < min_duration:
                os.remove(file_path)
                print(f"Vídeo apagado: {filename} ({duration:.2f} segundos)")

# Exemplo de uso
delete_short_videos("D:\\Sarau 09-03")
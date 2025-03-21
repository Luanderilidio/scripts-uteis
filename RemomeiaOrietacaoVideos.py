import os
import subprocess

def get_video_orientation(video_path):
    """
    Obtém a orientação do vídeo verificando suas dimensões.
    Retorna "vertical" se altura > largura, senão "horizontal".
    """
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0", video_path],
            capture_output=True, text=True, check=True
        )
        width, height = map(int, result.stdout.strip().split(','))
        return "vertical" if height > width else "horizontal"
    except Exception as e:
        print(f"Erro ao obter informações do vídeo {video_path}: {e}")
        return None

def rename_videos_by_orientation(folder_path):
    """
    Percorre uma pasta e renomeia os vídeos adicionando _vertical ou _horizontal
    conforme a orientação do vídeo.
    """
    if not os.path.exists(folder_path):
        print(f"A pasta {folder_path} não existe!")
        return
    
    video_extensions = ('.mp4', '.avi', '.mov', '.mkv', '.webm')
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path) and filename.lower().endswith(video_extensions):
            orientation = get_video_orientation(file_path)
            if orientation:
                new_filename = f"{os.path.splitext(filename)[0]}_{orientation}{os.path.splitext(filename)[1]}"
                new_file_path = os.path.join(folder_path, new_filename)
                os.rename(file_path, new_file_path)
                print(f"Renomeado: {filename} -> {new_filename}")

# Exemplo de uso
rename_videos_by_orientation(r"D:\PC Luander\Mondo Cani\Videos 1",)

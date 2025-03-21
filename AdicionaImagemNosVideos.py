import os
import subprocess

def add_logo_to_videos(folder_path, logo_path, output_folder):
    """
    Adiciona uma imagem sobreposta na parte inferior de todos os vídeos em uma pasta,
    redimensionando-a para caber no formato de story (1080x1920 pixels) usando FFmpeg.
    
    Args:
        folder_path (str): Caminho da pasta com os vídeos originais.
        logo_path (str): Caminho da imagem que será sobreposta.
        output_folder (str): Caminho da pasta onde os vídeos processados serão salvos.
    """
    STORY_WIDTH = 1080
    STORY_HEIGHT = 1920
    
    # Verificar se a pasta existe
    if not os.path.exists(folder_path):
        print(f"A pasta {folder_path} não existe!")
        return
    
    # Criar a pasta de saída, se não existir
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Processar cada vídeo da pasta
    video_extensions = ('.mp4', '.avi', '.mov', '.mkv', '.webm')
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path) and filename.lower().endswith(video_extensions):
            try:
                output_path = os.path.join(output_folder, filename)
                
                # Comando FFmpeg para redimensionar o vídeo e sobrepor a imagem na parte inferior
                command = [
                    "ffmpeg", "-i", file_path, "-i", logo_path,
                    "-filter_complex", 
                    f"[1:v]scale={STORY_WIDTH}:-1[overlay]; [0:v]scale={STORY_WIDTH}:{STORY_HEIGHT}[video]; [video][overlay]overlay=0:H-h",
                    "-c:v", "libx264", "-crf", "23", "-preset", "slow",
                    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", output_path
                ]
                
                subprocess.run(command, check=True)
                print(f"Vídeo processado com sucesso: {filename}")
            
            except subprocess.CalledProcessError as e:
                print(f"Erro ao processar {filename}: {e}")
# Exemplo de uso
add_logo_to_videos(
    folder_path= r"D:\PC Luander\Agras Tech\VIDEOS ALEATORIOS",
    logo_path= r"D:\PC Luander\Agras Tech\rodapé.png",
    output_folder=r"D:\PC Luander\Agras Tech\Videos_Com_Imagem"
)

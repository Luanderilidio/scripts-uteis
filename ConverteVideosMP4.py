import os
import subprocess

def convert_videos(input_folder, output_folder, output_format='mp4', codec='libx264'):
    """
    Converte todos os vídeos de uma pasta para um formato específico usando FFmpeg.
    
    :param input_folder: Caminho da pasta contendo os vídeos originais.
    :param output_folder: Caminho da pasta onde os vídeos convertidos serão salvos.
    :param output_format: Formato de saída dos vídeos (ex: 'mp4').
    :param codec: Codec de vídeo a ser usado (ex: 'libx264' para H.264).
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        
        if not os.path.isfile(input_path):
            continue  # Pula diretórios ou arquivos inválidos
        
        name, ext = os.path.splitext(filename)
        output_path = os.path.join(output_folder, f"{name}.{output_format}")
        
        command = [
            'ffmpeg', '-i', input_path, '-c:v', codec, '-preset', 'fast', '-c:a', 'aac', '-b:a', '192k', output_path
        ]
        
        print(f"Convertendo: {input_path} -> {output_path}")
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    print("Conversão concluída!")

# Configurações da conversão
input_folder = r"D:\PC Luander\Comercial da Roça\Midias - Bom dia\Videos"   # Substitua pelo caminho correto
output_folder = r"D:\PC Luander\Comercial da Roça\Midias - Bom dia\Video2"
convert_videos(input_folder, output_folder)

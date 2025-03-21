import os
import subprocess

def convert_files(input_folder, output_folder, output_format='mp3', codec='libmp3lame', bitrate='192k'):
    """
    Converte todos os arquivos de áudio de uma pasta para um formato específico usando FFmpeg.
    
    :param input_folder: Caminho da pasta contendo os arquivos originais.
    :param output_folder: Caminho da pasta onde os arquivos convertidos serão salvos.
    :param output_format: Formato de saída dos arquivos (ex: 'mp3').
    :param codec: Codec de áudio a ser usado (ex: 'libmp3lame' para MP3).
    :param bitrate: Taxa de bits do áudio de saída (ex: '192k').
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
            'ffmpeg', '-i', input_path, '-c:a', codec, '-b:a', bitrate, output_path
        ]
        
        print(f"Convertendo: {input_path} -> {output_path}")
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    print("Conversão concluída!")

# Configurações da conversão
input_folder = r"D:\PC Luander\Mondo Cani\Musicas"   # Substitua pelo caminho correto
output_folder = r"D:\PC Luander\Mondo Cani\Musicas_Convertidos"
convert_files(input_folder, output_folder)

from pytubefix import YouTube
from tqdm import tqdm
import os
import subprocess

def download_video_max_quality(video_url, output_folder='downloads'):
    os.makedirs(output_folder, exist_ok=True)  # Cria a pasta de saída, se não existir

    try:
        yt = YouTube(video_url)

        # Seleciona o stream de vídeo de maior qualidade
        video_stream = yt.streams.filter(adaptive=True, only_video=True).order_by('resolution').desc().first()
        # Seleciona o stream de áudio de maior qualidade
        audio_stream = yt.streams.filter(adaptive=True, only_audio=True).order_by('abr').desc().first()
        
        if not video_stream or not audio_stream:
            print("Não foi possível encontrar streams de vídeo e áudio separados.")
            return
        
    except Exception as e:
        print(f"Erro ao acessar o vídeo: {e}")
        return

    print(f"Baixando: {yt.title}")

    # Caminhos dos arquivos de vídeo e áudio
    video_file = os.path.join(output_folder, "video.mp4")
    audio_file = os.path.join(output_folder, "audio.mp4")
    output_file = os.path.join(output_folder, f"AULA 3 PYTHON.mp4")

    # Baixando o vídeo
    print("Baixando vídeo...")
    with tqdm(total=video_stream.filesize, unit='B', unit_scale=True, desc="Vídeo") as pbar:
        def progress_video(stream, chunk, bytes_remaining):
            pbar.update(video_stream.filesize - bytes_remaining - pbar.n)
        
        yt.register_on_progress_callback(progress_video)
        video_stream.download(output_path=output_folder, filename="video.mp4")

    # Baixando o áudio
    print("Baixando áudio...")
    with tqdm(total=audio_stream.filesize, unit='B', unit_scale=True, desc="Áudio") as pbar:
        def progress_audio(stream, chunk, bytes_remaining):
            pbar.update(audio_stream.filesize - bytes_remaining - pbar.n)
        
        yt.register_on_progress_callback(progress_audio)
        audio_stream.download(output_path=output_folder, filename="audio.mp4")

    # Mesclando vídeo e áudio com ffmpeg
    print("Mesclando vídeo e áudio...")
    command = [
        "ffmpeg", "-y",
        "-i", video_file,
        "-i", audio_file,
        "-c:v", "copy",  # Mantém o codec de vídeo original
        "-c:a", "aac",   # Codifica o áudio em AAC
        "-strict", "experimental",  # Garantir compatibilidade
        output_file
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Arquivo final salvo em: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao mesclar vídeo e áudio: {e}")

    # Remover arquivos intermediários (opcional)
    os.remove(video_file)
    os.remove(audio_file)

# Exemplo de uso
video_url = "https://www.youtube.com/watch?v=rRmDPXxt8OE"  # Substitua pela URL desejada
download_video_max_quality(video_url)

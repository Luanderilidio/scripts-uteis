import os
import random
import subprocess

def adicionar_audio_a_videos(pasta_videos, pasta_musicas, pasta_saida):
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)
    
    # Lista os arquivos de vídeo e áudio disponíveis
    videos = [f for f in os.listdir(pasta_videos) if f.endswith(('.mp4', '.mkv', '.avi'))]
    musicas = [f for f in os.listdir(pasta_musicas) if f.endswith('.mp3')]
    
    if not videos:
        print("Nenhum vídeo encontrado na pasta.")
        return
    
    if not musicas:
        print("Nenhuma música encontrada na pasta de músicas cortadas.")
        return
    
    for video in videos:
        caminho_video = os.path.join(pasta_videos, video)
        musica_escolhida = random.choice(musicas)
        caminho_musica = os.path.join(pasta_musicas, musica_escolhida)
        
        # Define o nome de saída
        novo_nome = f"{os.path.splitext(video)[0]}_com_audio.mp4"
        caminho_saida = os.path.join(pasta_saida, novo_nome)
        
        # Comando FFmpeg para adicionar o áudio ao vídeo, removendo faixas de áudio vazias
        cmd_adicionar_audio = [
            "ffmpeg", "-y", "-i", caminho_video, "-i", caminho_musica,
            "-map", "0:v:0", "-map", "1:a:0",  # Mapeia o vídeo e o áudio corretamente
            "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",  # Codifica áudio para AAC
            "-shortest", caminho_saida
        ]
        
        subprocess.run(cmd_adicionar_audio, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        print(f"Vídeo processado: {caminho_saida}")

        
diretorio_videos = r"D:\PC Luander\Agras Tech\Videos_Com_Imagem"
musica_fundo = r"D:\PC Luander\Agras Tech\Musicas"
diretorio_saida = r"D:\PC Luander\Agras Tech\Compilados"

# Chamada da função
adicionar_audio_a_videos(diretorio_videos, musica_fundo, diretorio_saida)

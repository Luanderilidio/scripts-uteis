import os
import random
import subprocess

def cortar_musica_ffmpeg(pasta_entrada, pasta_saida, duracao_max=30, partes=3):
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)
    
    for arquivo in os.listdir(pasta_entrada):
        if arquivo.endswith(('.mp3', '.wav', '.flac')):
            caminho_completo = os.path.join(pasta_entrada, arquivo)
            
            # Obtém a duração total do arquivo de áudio
            cmd_duracao = ["ffprobe", "-i", caminho_completo, "-show_entries", "format=duration", "-v", "quiet", "-of", "csv=p=0"]
            resultado = subprocess.run(cmd_duracao, capture_output=True, text=True)
            try:
                duracao_total = float(resultado.stdout.strip())
            except ValueError:
                print(f"Erro ao obter a duração de {arquivo}")
                continue
            
            for i in range(partes):
                inicio = random.uniform(0, max(0, duracao_total - duracao_max))
                novo_nome = f"{os.path.splitext(arquivo)[0]}_parte{i+1}.mp3"
                caminho_saida = os.path.join(pasta_saida, novo_nome)
                
                # Usa FFmpeg para cortar o áudio
                cmd_corte = [
                    "ffmpeg", "-i", caminho_completo, "-ss", str(inicio), "-t", str(duracao_max),
                    "-c", "copy", caminho_saida, "-y"
                ]
                subprocess.run(cmd_corte, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"Trecho salvo: {caminho_saida}")
# Defina as pastas de entrada e saída
diretorio_musicas = r"D:\PC Luander\Mondo Cani\Musicas"
diretorio_saida = r"D:\PC Luander\Mondo Cani\Musicas_Cortadas"

# Chamada da função
cortar_musica_ffmpeg(diretorio_musicas, diretorio_saida)

import re
import subprocess
import os

def processar_cortes_ffmpeg(input_video_path, cortes):
    """
    Processa múltiplos cortes de um vídeo usando ffmpeg diretamente.
    
    :param input_video_path: Caminho para o vídeo de entrada.
    :param cortes: Lista de strings no formato "NOME START-END - DESCRIÇÃO".
    """
    for corte in cortes:
        # Usar regex para extrair informações
        match = re.match(r"([\w-]+)\s([\d:]+)-([\d:]+)\s-\s(.+)", corte)
        if not match:
            print(f"Formato inválido: {corte}")
            continue
        
        # Nome base, tempo inicial, tempo final e descrição
        nome_base, start_time, end_time, descricao = match.groups()
        
        # Criar nome de saída baseado no nome base e na descrição
        descricao_limpa = descricao.replace(" ", "_").replace(",", "").replace(".", "")
        output_video_path = f"{nome_base}_{descricao_limpa}.mp4"
        
        # Cortar o vídeo usando ffmpeg
        print(f"Cortando: {descricao} ({start_time} a {end_time})")
        try:
            cortar_video_ffmpeg(input_video_path, output_video_path, start_time, end_time)
        except Exception as e:
            print(f"Erro ao processar {corte}: {e}")

def cortar_video_ffmpeg(input_video_path, output_video_path, start_time, end_time):
    """
    Realiza o corte de um vídeo usando ffmpeg diretamente.
    
    :param input_video_path: Caminho para o vídeo de entrada.
    :param output_video_path: Caminho para salvar o vídeo cortado.
    :param start_time: Tempo de início do corte (em formato HH:MM:SS).
    :param end_time: Tempo de término do corte (em formato HH:MM:SS).
    """
    comando = [
        "ffmpeg", "-i", input_video_path, "-ss", start_time, "-to", end_time,
        "-c", "copy", output_video_path, "-y"
    ]
    subprocess.run(comando, check=True)

# Exemplo de uso
input_video = "APARECIDA.MOV"
cortes = [
  "A4-TAKE-1 00:50-02:21 - FALA QUE OS PAIS DEIXARAM UM LEGADO PARA OS FILHOS",
  "A4-TAKE-2 02:22-03:53 - FALA QUE NA NOITE DE SÃO JOÃO A JOANA NASCEU",
  "A4-TAKE-3 04:33-06:37 - TUDO PARA ELA ERA JOÃO BATISTA, EXPRESSAVA MUITA FÉ, SE SENTIAM MAIS UNIDOS, FALA DAS COMIDAS TÍPICAS",
  "A4-TAKE-4 06:45-07:51 - A COMUNIDADE JÁ FICAVA AGUARDANDO A REZA, CONVITES",
  "A4-TAKE-5 08:03-09:30 - NO COMEÇO ERA FAMÍLIA, DEPOIS VIROU TRADIÇÃO",
  "A4-TAKE-6 10:45-12:00 - FALA DA ÚLTIMA REZA",
  "A4-TAKE-7 13:40-15:26 - FALA O QUANTO É BOM REZAR EM FAMÍLIA"
]

processar_cortes_ffmpeg(input_video, cortes)



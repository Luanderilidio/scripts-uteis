import re
from moviepy.video.io.VideoFileClip import VideoFileClip
import moviepy
print(moviepy.__version__)

def processar_cortes(input_video_path, cortes):
    """
    Processa múltiplos cortes de um vídeo com base em uma lista de especificações.
    
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
        
        # Cortar o vídeo
        print(f"Cortando: {descricao} ({start_time} a {end_time})")
        try:
            cortar_video(input_video_path, output_video_path, start_time, end_time)
        except Exception as e:
            print(f"Erro ao processar {corte}: {e}")

def cortar_video(input_video_path, output_video_path, start_time, end_time):
    """
    Realiza o corte de um vídeo no intervalo especificado e salva o resultado.
    
    :param input_video_path: Caminho para o vídeo de entrada.
    :param output_video_path: Caminho para salvar o vídeo cortado.
    :param start_time: Tempo de início do corte (em formato HH:MM:SS).
    :param end_time: Tempo de término do corte (em formato HH:MM:SS).
    """
    try:
        # Carregar o vídeo
        video = VideoFileClip(input_video_path)
        
        # Criar subclip
        subclip = video.subclip(t_start=start_time, t_end=end_time)
        
        # Exportar o subclip com qualidade original
        subclip.write_videofile(
            output_video_path,
            codec="libx264",       # Codec de vídeo de alta qualidade
            audio_codec="aac",     # Codec de áudio moderno e eficiente
            preset="ultrafast",    # Velocidade de exportação (alterar para "medium" para otimização)
            ffmpeg_params=["-crf", "0"]  # Define CRF 0 (Lossless Quality)
        )
    finally:
        # Liberar recursos
        video.close()
        if 'subclip' in locals():
            subclip.close()

# Exemplo de uso
input_video = "IMG_8961.MOV"
cortes = [
    "A1-TAKE-1 00:55-02:20 - COMEÇOU A VIDA NA IGREJA CATÓLICA",
    "A1-TAKE-2 02:25-03:00 - COMEÇOU A SER REZADEIRA",
    "A1-TAKE-3 03:00-05:20 - NINGUÉM QUER REZAR, NÃO RESPONDEM",
    "A1-TAKE-4 05:20-06:35 - SOBRE OS JOVENS, NÃO QUEREM, ATRAPALHAM",
    "A1-TAKE-5 06:40-09:20 - SOBRE A REZA DA DONA MARIA",
    "A1-TAKE-6 10:05-10:22 - COMO CONHECEU DONA MARIA",
    "A1-TAKE-7 11:35-12:22 - VAI MAIS MULHER DO QUE HOMEM NA REZA",
    "A1-TAKE-8 12:51-13:18 - DONA MARIA VISITA JEFA, MORTE DA MÃE",
    "A1-TAKE-9 14:18-14:35 - FALA DO SEU GODOFREDO",
    "A1-TAKE-10 16:50-18:30 - FALA DAS PROCISÕES",
    "A1-TAKE-11 19:50-21:30 - FALA DA FALTA DAS REZADEIRA",
    "A1-TAKE-12 21:30-22:20 - VOCAÇÃO PARA SER REZADEIRA",
    "A1-TAKE-13 22:50-24:00 - FALA QUE ANTIGAMENTE TINHA BASTANTE REZA",
    "A1-TAKE-14 25:09-25:40 - FALA QUE ACABOU AS REZAS",
    "A1-TAKE-15 25:40-26:25 - FALA COMO COMEÇOU A SER REZADEIRA",
    "A1-TAKE-16 27:55-28:30 - FALA DO CADERNO DE REZADEIRA",
]

# Processar os cortes
processar_cortes(input_video, cortes)

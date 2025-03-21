import os
import random
import shutil
from tqdm import tqdm  # Barra de progresso

# Configurações
pasta_origem = r"D:\PC Luander\Fast Escova\Videos"  # Pasta onde estão os vídeos originais
pasta_destino = r"D:\PC Luander\Fast Escova\PAST_ALEATORIOS"  # Pasta onde serão criadas as 30 pastas
num_pastas = 30  # Número de pastas a serem criadas
videos_por_pasta = 10  # Número de vídeos por pasta

# Obtém a lista de vídeos na pasta de origem
videos = [f for f in os.listdir(pasta_origem) if os.path.isfile(os.path.join(pasta_origem, f))]

# Verifica se há vídeos disponíveis
if not videos:
    print("❌ Nenhum vídeo encontrado na pasta de origem.")
else:
    os.makedirs(pasta_destino, exist_ok=True)  # Criar pasta de destino se não existir
    total_videos = num_pastas * videos_por_pasta  # Total de cópias de vídeos a serem feitas
    progresso = tqdm(total=total_videos, desc="Processando vídeos", unit="vídeo")  # Barra de progresso

    # Embaralha a ordem das pastas
    pastas = list(range(1, num_pastas + 1))
    random.shuffle(pastas)

    for pasta_num in pastas:
        nome_pasta = os.path.join(pasta_destino, f"pasta_{pasta_num:02d}")
        os.makedirs(nome_pasta, exist_ok=True)

        # Embaralha a lista de vídeos para garantir a seleção aleatória
        videos_embaralhados = random.sample(videos, len(videos))  # Embaralha os vídeos

        # Escolhe 8 vídeos aleatórios para essa pasta
        for j in range(videos_por_pasta):
            video = videos_embaralhados[j]  # Seleciona um vídeo aleatório da lista embaralhada
            origem = os.path.join(pasta_origem, video)
            destino = os.path.join(nome_pasta, video)

            # Copia o arquivo original
            shutil.copy(origem, destino)

            # Atualiza a barra de progresso
            progresso.update(1)

    progresso.close()
    print("🎬 Todos os vídeos foram copiados para as pastas!")

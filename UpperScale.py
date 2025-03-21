
import cv2
import os
from tqdm import tqdm

def melhorar_imagens_em_pasta(caminho_pasta):
    # Verificar se o caminho da pasta é válido
    if not os.path.isdir(caminho_pasta):
        raise ValueError("Caminho da pasta inválido. Verifique o caminho.")

    # Criar uma pasta de saída para salvar as imagens processadas
    caminho_saida = os.path.join(caminho_pasta, "imagens_melhoradas")
    os.makedirs(caminho_saida, exist_ok=True)

    # Carregar o modelo de super-resolução
    modelo = "FSRCNN_x4.pb"  # Substitua por outro modelo se desejar
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel(modelo)

    # Configurar o fator de escala do modelo
    sr.setModel("fsrcnn", 4)  # "fsrcnn" com aumento de 4x

    # Listar todas as imagens na pasta
    arquivos = [f for f in os.listdir(caminho_pasta) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    # Processar cada imagem com uma barra de progresso
    for arquivo in tqdm(arquivos, desc="Processando imagens"):
        caminho_imagem = os.path.join(caminho_pasta, arquivo)

        # Verificar se o arquivo é realmente uma imagem usando OpenCV
        try:
            imagem_teste = cv2.imread(caminho_imagem)
            if imagem_teste is None:
                print(f"Aviso: O arquivo {arquivo} não é uma imagem válida. Pulando...")
                continue
        except Exception as e:
            print(f"Erro ao verificar o arquivo {arquivo}: {e}. Pulando...")
            continue

        # Carregar a imagem
        imagem = cv2.imread(caminho_imagem)

        # Verificar se a imagem foi carregada corretamente
        if imagem is None:
            print(f"Aviso: Não foi possível carregar a imagem {arquivo}. Pulando...")
            continue

        # Garantir que a imagem tenha 3 canais (BGR)
        if len(imagem.shape) < 3 or imagem.shape[2] != 3:
            imagem = cv2.cvtColor(imagem, cv2.COLOR_GRAY2BGR)

        # Aplicar super-resolução à imagem
        try:
            imagem_melhorada = sr.upsample(imagem)
        except Exception as e:
            print(f"Erro ao processar a imagem {arquivo}: {e}. Pulando...")
            continue

        # Salvar a imagem processada na pasta de saída
        caminho_imagem_saida = os.path.join(caminho_saida, arquivo)
        cv2.imwrite(caminho_imagem_saida, imagem_melhorada)

    print(f"Imagens processadas e salvas em: {caminho_saida}")

melhorar_imagens_em_pasta("Fotos")
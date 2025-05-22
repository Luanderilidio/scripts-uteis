import os
from rembg import remove
from PIL import Image
from tqdm import tqdm
import io

def remover_fundo_adicionar_branco(input_path, output_path):
    with Image.open(input_path) as img:
        img = img.convert("RGBA")

        # Converte imagem para bytes (necessário para rembg)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_bytes = buffer.getvalue()

        # Remove fundo
        output_bytes = remove(img_bytes)

        # Reabre como imagem PIL
        img_sem_fundo = Image.open(io.BytesIO(output_bytes)).convert("RGBA")

        # Cria fundo branco
        fundo_branco = Image.new("RGBA", img_sem_fundo.size, (255, 255, 255, 255))

        # Mescla fundo branco
        img_com_fundo_branco = Image.alpha_composite(fundo_branco, img_sem_fundo)

        # Converte para RGB (obrigatório para JPG)
        img_final = img_com_fundo_branco.convert("RGB")

        # Salva como JPG
        img_final.save(output_path, format="JPEG")

def processar_diretorio(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    imagens = [f for f in os.listdir(input_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    for filename in tqdm(imagens, desc="Processando imagens"):
        input_path = os.path.join(input_dir, filename)
        output_filename = os.path.splitext(filename)[0] + "_semfundo.jpg"
        output_path = os.path.join(output_dir, output_filename)
        remover_fundo_adicionar_branco(input_path, output_path)

# Diretórios
input_dir = r'D:\CLIENTES LEB\11-Ativos_Contabilidade\Fotos-Ativos_Contabilidade'
output_dir = r'D:\CLIENTES LEB\11-Ativos_Contabilidade\Fotos-Ativos_RemoveBG'

# Iniciar processamento
processar_diretorio(input_dir, output_dir)

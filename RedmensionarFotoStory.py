from PIL import Image, ImageDraw, ImageOps
import os

def add_logo_to_images(folder_path, logo_path, output_folder):
    """
    Adiciona uma logo no canto superior direito de todas as imagens em uma pasta,
    redimensionando as imagens para o formato de story (1080x1920 pixels) com zoom para preencher o frame completamente.
    
    Args:
        folder_path (str): Caminho da pasta com as imagens originais.
        logo_path (str): Caminho da logo que será adicionada.
        output_folder (str): Caminho da pasta onde as imagens processadas serão salvas.
    """
    STORY_SIZE = (1080, 1920)  # Resolução de stories no Instagram

    # Verificar se a pasta existe
    if not os.path.exists(folder_path):
        print(f"A pasta {folder_path} não existe!")
        return
    
    # Criar a pasta de saída, se não existir
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Abrir a logo
    logo = Image.open(logo_path).convert("RGBA")
    logo_width, logo_height = logo.size
    
    # Processar cada imagem da pasta
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp')
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path) and filename.lower().endswith(image_extensions):
            try:
                # Abrir a imagem
                image = Image.open(file_path).convert("RGBA")

                # Redimensionamento com zoom para story
                ratio = max(STORY_SIZE[0] / image.size[0], STORY_SIZE[1] / image.size[1])
                new_size = (int(image.size[0] * ratio), int(image.size[1] * ratio))
                image = image.resize(new_size, Image.Resampling.LANCZOS)

                # Cortar para o tamanho exato do story
                left = (image.size[0] - STORY_SIZE[0]) / 2
                top = (image.size[1] - STORY_SIZE[1]) / 2
                right = left + STORY_SIZE[0]
                bottom = top + STORY_SIZE[1]
                image = image.crop((left, top, right, bottom))

                # Ajustar o tamanho da logo
                scale_factor = 0.2
                new_logo_width = int(STORY_SIZE[0] * scale_factor)
                new_logo_height = int(logo_height * (new_logo_width / logo_width))
                resized_logo = logo.resize((new_logo_width, new_logo_height), Image.Resampling.LANCZOS)
                
                # Posição da logo (canto superior direito)
                margin_top = 5
                margin_right = 5
                position = (STORY_SIZE[0] - new_logo_width - margin_right, margin_top)

                # Colar a logo na imagem
                image.paste(resized_logo, position, resized_logo)
                
                # Converter para RGB e salvar
                output_path = os.path.join(output_folder, filename)
                image.convert("RGB").save(output_path, "JPEG", quality=95)
                print(f"Imagem processada com sucesso: {filename}")

            except Exception as e:
                print(f"Erro ao processar {filename}: {e}")

# Exemplo de uso
add_logo_to_images(
    folder_path="Fotos",
    logo_path="LOGO_BRANCA_MFIT.png",
    output_folder="Fotos Story"
)

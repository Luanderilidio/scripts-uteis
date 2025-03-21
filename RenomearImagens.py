import os
import uuid

def rename_images_and_change_extension(folder_path, new_extension):
    """
    Renomeia todas as imagens em uma pasta com o padrão IMG_<UUID4> e troca a extensão.

    Args:
        folder_path (str): Caminho da pasta com as imagens.
        new_extension (str): Nova extensão para os arquivos (ex: ".png").
    """
    # Verificar se a pasta existe
    if not os.path.exists(folder_path):
        print(f"A pasta {folder_path} não existe!")
        return
    
    # Extensões de imagem comuns
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp')
    
    try:
        # Percorrer todos os arquivos na pasta
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            # Verificar se é um arquivo e se tem uma extensão de imagem
            if os.path.isfile(file_path) and filename.lower().endswith(image_extensions):
                # Gerar um UUID reduzido de 4 caracteres
                short_uuid = str(uuid.uuid4())[:4]
                
                # Criar um novo nome com o UUID curto e a nova extensão
                new_filename = f"01 - IMG_{short_uuid}{new_extension}"
                new_file_path = os.path.join(folder_path, new_filename)

                # Renomear o arquivo
                os.rename(file_path, new_file_path)
                print(f"Renomeado: {filename} -> {new_filename}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


# Exemplo de uso
rename_images_and_change_extension("Fotos Story", ".png")

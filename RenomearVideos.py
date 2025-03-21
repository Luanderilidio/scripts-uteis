import os
import uuid

def rename_videos(folder_path):
    """
    Renomeia todos os vídeos em uma pasta com o padrão VID_<UUID4> (4 caracteres).

    Args:
        folder_path (str): Caminho da pasta com os vídeos.
    """
    # Verificar se a pasta existe
    if not os.path.exists(folder_path):
        print(f"A pasta {folder_path} não existe!")
        return
    
    # Extensões de vídeo comuns
    video_extensions = ('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv')
    
    try:
        # Percorrer todos os arquivos na pasta
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            # Verificar se é um arquivo e se tem uma extensão de vídeo
            if os.path.isfile(file_path) and filename.lower().endswith(video_extensions):
                # Gerar um UUID reduzido de 4 caracteres
                short_uuid = str(uuid.uuid4())[:4]
                
                # Criar um novo nome com o UUID curto
                new_filename = f"VID_{short_uuid}{os.path.splitext(filename)[1]}"
                new_file_path = os.path.join(folder_path, new_filename)

                # Renomear o arquivo
                os.rename(file_path, new_file_path)
                print(f"Renomeado: {filename} -> {new_filename}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")



rename_videos(r"D:\PC Luander\Agras Tech\VIDEOS ALEATORIOS",)

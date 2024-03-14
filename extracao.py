import os
import shutil

# Definir os diretórios de entrada e saída
input_folder_mature = 'TomatesMaduros'
input_folder_green = 'TomatesVerdes'
output_folder_mature = 'Tomates Maduros'
output_folder_green = 'Tomates Verdes'

# Função para extrair e salvar imagens
def extract_and_save_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Listar todos os arquivos e diretórios na pasta de entrada
    files_and_dirs = os.listdir(input_folder)
    
    # Iterar sobre cada arquivo ou diretório na pasta de entrada
    for item in files_and_dirs:
        # Construir o caminho completo para o item
        item_path = os.path.join(input_folder, item)
        
        # Verificar se o item é um arquivo
        if os.path.isfile(item_path) and item.endswith('.jpg'):
            # Copiar o arquivo para a pasta de saída
            shutil.copy(item_path, output_folder)
        # Verificar se o item é um diretório
        elif os.path.isdir(item_path):
            # Iterar sobre os arquivos dentro do diretório
            for file in os.listdir(item_path):
                # Verificar se o arquivo é uma imagem
                if file.endswith('.jpg'):
                    # Construir o caminho completo para o arquivo de imagem
                    image_path = os.path.join(item_path, file)
                    # Copiar o arquivo de imagem para a pasta de saída
                    shutil.copy(image_path, output_folder)

# Extrair e salvar imagens de tomates maduros
extract_and_save_images(input_folder_mature, output_folder_mature)

# Extrair e salvar imagens de tomates verdes
extract_and_save_images(input_folder_green, output_folder_green)

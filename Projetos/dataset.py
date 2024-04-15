from google_images_search import GoogleImagesSearch
import os

# Configurar a API de busca do Google
google_search_engine_id = "d6c56700e99b449d1"
google_api_key = '526659027729-eo70ghot0stqcbs5t0nblen1cj2npuom.apps.googleusercontent.com'

# Configurar os diretórios de saída
output_folder_mature = 'TomatesMaduros'
output_folder_green = 'TomatesVerdes'

# Função para fazer o download das imagens
def download_images(query, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Inicializar o GoogleImagesSearch com as credenciais
    gis = GoogleImagesSearch(google_api_key, google_search_engine_id)

    # Configurar os parâmetros de busca
    search_params = {
        'q': query,
        'num': 100,  # número máximo de resultados
        'safe': 'medium',  # filtro de segurança
        'fileType': 'jpg'  # tipo de arquivo
    }

    # Executar a busca
    gis.search(search_params=search_params)

    # Fazer o download das imagens
    for i, image in enumerate(gis.results(), 1):
        image.download(os.path.join(output_folder, f"{query.replace(' ', '_')}_{i}.jpg"))

# Fazer o download das imagens de tomates maduros
download_images('tomates maduros', output_folder_mature)

# Fazer o download das imagens de tomates verdes
download_images('tomates verdes', output_folder_green)





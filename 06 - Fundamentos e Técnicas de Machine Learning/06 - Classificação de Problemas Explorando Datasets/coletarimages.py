# Instale primeiro a biblioteca:
# pip install icrawler

from icrawler.builtin import BingImageCrawler

def baixar_imagens(classe, pasta, quantidade=100):
    """
    Baixa imagens da internet usando Bing e salva em uma pasta específica.
    
    classe: termo de busca (ex.: 'tomate verde')
    pasta: nome da pasta onde salvar (ex.: 'dataset/tomate_verde')
    quantidade: número de imagens a baixar (default=100)
    """
    crawler = BingImageCrawler(storage={"root_dir": pasta})
    crawler.crawl(keyword=classe, max_num=quantidade)

# Exemplo de uso:
baixar_imagens("tomate verde", "dataset/tomate_verde", quantidade=100)
baixar_imagens("tomate maduro", "dataset/tomate_maduro", quantidade=100)

# Você pode adicionar outras classes facilmente:
# baixar_imagens("cachorro", "dataset/cachorro", quantidade=200)
# baixar_imagens("gato", "dataset/gato", quantidade=200)
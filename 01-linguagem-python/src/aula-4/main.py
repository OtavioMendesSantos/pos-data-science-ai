import pandas as pd;
import matplotlib.pyplot as plt
import os

arquive_path = './Iris.csv'

# Carregar arquivo
def carregar_arquivo(path):
    dados = None
    
    try: 
        dados = pd.read_csv(path)
    except:
        print("Arquivo não encontrado.")
    
    return dados
    
# tratamento do arquivo
def carregar_arquivo(path):
    print("Carregando arquivo...")
    try: 
        dados = pd.read_csv(path)
        return dados
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return None

def tratamento_arquivo(archive):
    # Códigos ANSI para cores
    COR_AZUL = '\033[94m'
    COR_VERDE = '\033[92m'
    RESETAR = '\033[0m'
    
    print(f"\n{COR_AZUL}{'='*60}{RESETAR}")
    print(f"{COR_AZUL}[INFO] Iniciando agrupamento de dados...{RESETAR}")
    print(f"{COR_AZUL}{'='*60}{RESETAR}\n")
    
    if 'Id' in archive.columns:
        archive = archive.drop(columns=['Id'])
        
    medias_por_especie = archive.groupby('Species').mean()
    
    print("[RESULTADO] Médias das características por espécie:")
    print("-" * 60)
    print(medias_por_especie.to_string()) 
    print("-" * 60)
    
    print(f"\n{COR_VERDE}[OK] Tratamento concluído com sucesso!{RESETAR}\n")
        
# analise de dados
def analise_dados(archive):
    print(archive)

if __name__ == '__main__':
    os.system('clear')
    print("Carregando arquivo...")
    arquivo = carregar_arquivo(arquive_path)
    tratamento_arquivo(arquivo)
    
import os
import sys
from dotenv import load_dotenv


load_dotenv()


sys.path.append(os.getcwd())

def setup():
    print("Iniciando ingestão dos SEUS PDFs (Davi)...")

    try:
        from app.agents.davi_agent import knowledge_base
        
      
        if not os.path.exists("pdfs_davi"):
            print("AVISO: A pasta 'pdfs_davi' não foi encontrada na raiz!")
            print("Certifique-se de que seus PDFs estão na pasta correta.")
        
        knowledge_base.load(recreate=True)
        
        print("SUCESSO! Banco de dados de Produtos Gerais (Davi) criado e populado.")

    except ImportError as e:
        print("Erro de Importação: Não consegui encontrar o arquivo 'davi_agent.py'.")
        print(f"Detalhe: {e}")
        print("Verifique se ele está na pasta 'app/agents/'.")
    except Exception as e:
        print(f"Erro durante a ingestão: {e}")

if __name__ == "__main__":
    setup()
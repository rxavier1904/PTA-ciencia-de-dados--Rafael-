import os
import sys
from dotenv import load_dotenv

# Carrega as variáveis de ambiente (.env)
load_dotenv()

# Adiciona o diretório atual ao sistema para conseguir importar o app
sys.path.append(os.getcwd())

def setup():
    print("🚀 Iniciando ingestão dos SEUS PDFs (Davi)...")

    try:
        # Importa a knowledge_base configurada no seu arquivo davi_agent.py
        # IMPORTANTE: O Python precisa achar o arquivo app/agents/davi_agent.py
        from app.agents.davi_agent import knowledge_base
        
        # Verifica se a pasta de PDFs existe (baseado no seu código anterior)
        if not os.path.exists("pdfs_davi"):
            print("⚠️ AVISO: A pasta 'pdfs_davi' não foi encontrada na raiz!")
            print("Certifique-se de que seus PDFs estão na pasta correta.")
        
        # Inicia a leitura e gravação no ChromaDB
        # recreate=True garante que ele apague o antigo (LanceDB ou corrompido) e crie um novo limpo
        knowledge_base.load(recreate=True)
        
        print("✅ SUCESSO! Banco de dados de Produtos Gerais (Davi) criado e populado.")

    except ImportError as e:
        print("❌ Erro de Importação: Não consegui encontrar o arquivo 'davi_agent.py'.")
        print(f"Detalhe: {e}")
        print("Verifique se ele está na pasta 'app/agents/'.")
    except Exception as e:
        print(f"❌ Erro durante a ingestão: {e}")

if __name__ == "__main__":
    setup()
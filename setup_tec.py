from dotenv import load_dotenv
load_dotenv()

import os
import sys
from pathlib import Path

# Adiciona o diretório atual ao sistema
sys.path.append(os.getcwd())

def setup():
    print("🚀 Verificando pasta 'pdfs_gabriel' na raiz...")
    
    # 1. Verifica se a pasta existe
    base_path = Path("pdfs_gabriel")
    if not base_path.exists():
        print(f"❌ ERRO: A pasta '{base_path.absolute()}' não existe!")
        return

    # 2. Verifica arquivos
    pdf_files = list(base_path.rglob("*.pdf"))
    print(f"📂 Encontrados {len(pdf_files)} PDFs na pasta do Gabriel.")

    print("🚀 Iniciando leitura e indexação (Isso pode demorar)...")
    
    try:
        # Importa o knowledge que acabamos de corrigir no passo 1
        from app.knowledge.tec_pdf_kb import tec_knowledge
        
        # Inicia a ingestão
        tec_knowledge.load(recreate=True)
        
        print("✅ SUCESSO! O 'tec_agente' agora sabe tudo sobre os PDFs do Gabriel.")

    except Exception as e:
        print(f"❌ Erro durante a ingestão: {e}")

if __name__ == "__main__":
    setup()
from dotenv import load_dotenv
load_dotenv()

import os
import sys
from pathlib import Path


sys.path.append(os.getcwd())

def setup():
    print("Verificando pasta 'pdfs_gabriel' na raiz...")
    

    base_path = Path("pdfs_gabriel")
    if not base_path.exists():
        print(f"ERRO: A pasta '{base_path.absolute()}' não existe!")
        return


    pdf_files = list(base_path.rglob("*.pdf"))
    print(f"Encontrados {len(pdf_files)} PDFs na pasta.")

    print("Iniciando leitura e indexação (Isso pode demorar)...")
    
    try:
        from app.knowledge.tec_pdf_kb import tec_knowledge
        
  
        tec_knowledge.load(recreate=True)
        
        print("SUCESSO! O agente agora sabe tudo sobre os PDFs")

    except Exception as e:
        print(f"Erro durante a ingestão: {e}")

if __name__ == "__main__":
    setup()
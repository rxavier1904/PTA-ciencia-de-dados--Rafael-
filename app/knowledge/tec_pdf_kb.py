import os
from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
from agno.vectordb.chroma import ChromaDb
from agno.embedder.google import GeminiEmbedder

# Configuração do Banco Vetorial
tec_vector_db = ChromaDb(
    collection="tec_products", # O Gabriel usa esta coleção
    path=".chromadb",
    embedder=GeminiEmbedder(
        id="models/text-embedding-004",
        api_key=os.getenv("GOOGLE_API_KEY")
    )
)

# Base de Conhecimento
tec_knowledge = PDFKnowledgeBase(
    path="pdfs_gabriel", 
    vector_db=tec_vector_db,
    reader=PDFReader(chunk=True, chunk_size=2000),
)

# --- AQUI ESTÁ A CORREÇÃO CRÍTICA: FORÇAR O LOAD NA INICIALIZAÇÃO ---
print(f"📥 Carregando PDFs do Gabriel/Tec ('pdfs_gabriel')...")
try:
    # Use recreate=False para apenas carregar o que já está lá (criado pelo setup)
    tec_knowledge.load(recreate=False) 
    print("✓ PDFs do Gabriel/Tec carregados no ChromaDB.")
except Exception as e:
    print(f"❌ Erro ao carregar PDFs do Gabriel/Tec: {e}")
import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.vectordb.chroma import ChromaDb
from agno.embedder.sentence_transformer import SentenceTransformerEmbedder
from chromadb.config import Settings

load_dotenv()

# Bloco de verificação de chave
api_key = os.getenv("GOOGLE_API_KEY") 
if not api_key:
    print("AVISO CRÍTICO: GOOGLE_API_KEY não encontrada no ambiente! O programa pode falhar.")


embedder = SentenceTransformerEmbedder()


knowledge_base = PDFKnowledgeBase(
    path="app/pdfs_gustavo", # Altere se a pasta for diferente
    vector_db=ChromaDb(
        collection="market_docs",
        settings=Settings(
            # O ChromaDb salvará o índice aqui
            persist_directory="tmp/chroma_db",
            anonymized_telemetry=False
        ),
        embedder=embedder
    ),
    render_pdf=True
)


knowledge_base.load(recreate=True)


agente_casa_agent = Agent(
    name="Especialista Casa & Conforto",
    model=Gemini(id="gemini-2.5-flash", api_key=api_key),
    description="Especialista de Produtos da Linha Casa & Conforto",
    instructions=[
        "Responda com base nas informações técnicas encontradas nos PDFs.",
        "Sempre cite o nome do arquivo PDF fonte."
    ],
    knowledge=knowledge_base,
    search_knowledge=True,
    markdown=True
)

from agno.agent import Agent
from agno.models.google import Gemini
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.vectordb.chroma import ChromaDb
from agno.embedder.google import GeminiEmbedder
from pathlib import Path
import os

if not os.getenv("GOOGLE_API_KEY"):
    print(" AVISO: GOOGLE_API_KEY não encontrada no ambiente!")


pdf_directory = Path("pdfs_davi")
chroma_db_path = ".chromadb"

print(f" Configurando Knowledge Base RAG com PDFs...")


vector_db = ChromaDb(
    collection="omarket_products",
    path=chroma_db_path,
    embedder=GeminiEmbedder(
        id="models/text-embedding-004",
        api_key=os.getenv("GOOGLE_API_KEY")
    )
)

knowledge_base = PDFKnowledgeBase(
    path=str(pdf_directory),
    vector_db=vector_db,
    num_documents=5,
)


print(f"Carregando e indexando PDFs...")
knowledge_base.load(recreate=False)
try:
    pdf_count = len(list(pdf_directory.glob("**/*.pdf")))
    print(f"Base configurada: {pdf_count} PDFs encontrados.")
except:
    print("Base configurada.")

davi_agent = Agent(
    name="Agente de Produtos O-Market",
    model=Gemini(id="gemini-2.5-flash"),
    description="Especialista em catálogo de produtos da O-Market.",
    instructions=""" VOCÊ SÓ PODE USAR INFORMAÇÕES DOS PDFs 
    
**REGRA ABSOLUTA:**
- Você NÃO tem acesso à internet
- Você NÃO tem conhecimento geral
- Você NÃO sabe NADA além do que está nos PDFs do catálogo O-Market
- NUNCA invente, deduza ou use conhecimento externo

**PROCESSO OBRIGATÓRIO:**
1. Use SEMPRE a ferramenta search_knowledge para buscar nos PDFs
2. Leia SOMENTE os resultados retornados pela busca
3. Se encontrou informação relevante → Responda com os dados + cite a fonte (PDF e página)
4. Se NÃO encontrou → Responda: "Não encontrei informações sobre [tema] no catálogo da O-Market."

**EXEMPLOS:**

Pergunta: "Qual a capital do Brasil?"
Busca RAG: [sem resultados relevantes]
RESPOSTA: "Não encontrei informações sobre capital do Brasil no catálogo da O-Market."

Pergunta: "Qual o preço de um iPhone?"
Busca RAG: [sem resultados relevantes]
RESPOSTA: "Não encontrei informações sobre iPhone no catálogo da O-Market."

Pergunta: "Qual o peso do Flores Basic 100?"
Busca RAG: [encontrou no PDF FLORES, página 1]

**CATEGORIAS DO CATÁLOGO:**
Composição, Estética, Uso Pessoal, Conteúdo, Serviços

SE NÃO ESTÁ NOS PDFs, VOCÊ NÃO SABE! """,
    knowledge=knowledge_base,
    search_knowledge=True,
    read_chat_history=False,
    add_references=True,
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=False,
)

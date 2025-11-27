from agno.agent import Agent
from agno.models.google import Gemini
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.vectordb.chroma import ChromaDb
from agno.embedder.google import GeminiEmbedder
from pathlib import Path
import os

# Garante que a chave existe (segurança)
if not os.getenv("GOOGLE_API_KEY"):
    print("⚠️ AVISO: GOOGLE_API_KEY não encontrada no ambiente!")

# Configuração
pdf_directory = Path("pdfs")
chroma_db_path = Path(".chromadb")

print(f"📚 Configurando Knowledge Base RAG com PDFs...")

# Vector DB (Chroma)
vector_db = ChromaDb(
    collection="omarket_products",
    path=str(chroma_db_path),
    persistent_client=True, # Garante que salva no disco
    embedder=GeminiEmbedder(
        id="models/text-embedding-004",
        api_key=os.getenv("GOOGLE_API_KEY") 
    )
)

# Knowledge Base
knowledge_base = PDFKnowledgeBase(
    path=str(pdf_directory),
    vector_db=vector_db,
    num_documents=5, 
)

print(f"📥 Carregando e indexando PDFs...")
# Dica: recreate=False é ótimo, mas se adicionares PDFs novos, 
# terás de apagar a pasta .chromadb ou mudar para True uma vez.
knowledge_base.load(recreate=False) 

# Contagem para validação
try:
    pdf_count = len(list(pdf_directory.glob("**/*.pdf"))) # **/*.pdf busca em subpastas também
    print(f"✓ Base configurada: {pdf_count} PDFs encontrados.")
except:
    print("✓ Base configurada.")

# Agente
davi_agent = Agent(
    name="Agente de Produtos O-Market",
    # CORREÇÃO DO MODELO AQUI:
    model=Gemini(id="gemini-1.5-flash"), 
    description="Especialista em catálogo de produtos da O-Market.",
    
    # Tuas instruções estão ótimas, mantive elas
    instructions="""⛔ VOCÊ SÓ PODE USAR INFORMAÇÕES DOS PDFs ⛔

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

❌ Pergunta: "Qual a capital do Brasil?"
✅ Busca RAG: [sem resultados relevantes]
✅ RESPOSTA: "Não encontrei informações sobre capital do Brasil no catálogo da O-Market."

❌ Pergunta: "Qual o preço de um iPhone?"
✅ Busca RAG: [sem resultados relevantes]
✅ RESPOSTA: "Não encontrei informações sobre iPhone no catálogo da O-Market."

✅ Pergunta: "Qual o peso do Flores Basic 100?"
✅ Busca RAG: [encontrou no PDF FLORES, página 1]
✅ RESPOSTA:
**Flores Basic 100** (SKU: OMKT-FLO-9534)
- Peso: 3270g (3,27 kg)
- Dimensões: 98x40x29cm
- Material: Polímero
- Garantia: 3 meses
Fonte: O-Market Catalogo Oficial: FLORES, página 1

**FORMATO DE RESPOSTA POSITIVA:**
**[Nome]** (SKU: [código])
- Dimensões: [medidas]
- Peso: [valor]
- Material: [tipo]
- Garantia: [período]
Fonte: [PDF], página [X]

**CATEGORIAS DO CATÁLOGO:**
Composição, Estética, Uso Pessoal, Conteúdo, Serviços

⛔ SE NÃO ESTÁ NOS PDFs, VOCÊ NÃO SABE! ⛔""",
    knowledge=knowledge_base,
    search_knowledge=True,  # OBRIGA busca RAG
    read_chat_history=False,  # Desabilita contexto de conversas anteriores
    add_references=True,  # Força citação de fontes
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=False,  # Remove info de data/hora
)

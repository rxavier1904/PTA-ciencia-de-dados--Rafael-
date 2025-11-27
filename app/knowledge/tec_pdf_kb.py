from agno.embedder.google import GeminiEmbedder
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
from dotenv import load_dotenv
load_dotenv()


tec_vector_db = LanceDb(
    uri="app/data/lancedb",
    table_name="tec_products",
    search_type=SearchType.vector,
    embedder=GeminiEmbedder(),
)

tec_knowledge = PDFKnowledgeBase(
    path="app/data/pdfs/tec",
    vector_db=tec_vector_db,
    reader=PDFReader(),
)

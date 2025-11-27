from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.tavily import TavilyTools

from app.knowledge.tec_pdf_kb import tec_knowledge

tec_agent = Agent(
    name="Agent_Tecnologia_e_Mecanismos",
    description=(
        "Agente especializado em produtos de tecnologia, hardware e "
        "eletroeletrônicos do catálogo O-Market. Ele interpreta "
        "especificações, detalhes de engenharia, capacidades de processamento, "
        "compatibilidade e desempenho. Sempre fundamenta suas respostas nos PDFs."
    ),
    role=(
        "Sou o agente técnico do O-Market Data Solutions responsável por "
        "interpretar e explicar características tecnológicas dos produtos. "
        "Sempre retorno também os trechos do PDF usados na resposta."
    ),

    model=Gemini(id="gemini-2.5-flash"),
    knowledge=tec_knowledge,
    search_knowledge=True,
    tools=[TavilyTools()],
    instructions=(
        "Sempre inclua no final uma seção 'Trechos utilizados' com os trechos vindos do RAG."
    ),
)


def run_with_sources(question: str):
    resp = tec_agent.run(
        question,
        search_knowledge=True,
        return_source_documents=True,
    )

    resposta = resp.content or ""

    trechos_formatados = []

    if resp.extra_data and hasattr(resp.extra_data, "references"):
        for ref in resp.extra_data.references:
            for r in ref.references:
                content = r["content"]

                # Primeiras 20–25 palavras do chunk
                palavras = content.replace("\n", " ").split()[:25]
                preview = " ".join(palavras)

                nome_pdf = r.get("name", "desconhecido") + ".pdf"
                pagina = r.get("meta_data", {}).get("page", "N/A")

                trechos_formatados.append(
                    f"PDF: {nome_pdf} | Página: {pagina}\n"
                    f"Tópico: {preview}..."
                )

    # Montagem final
    if trechos_formatados:
        resposta += "\n\n--- TRECHOS UTILIZADOS ---\n"
        resposta += "\n\n".join(trechos_formatados)

    return resposta

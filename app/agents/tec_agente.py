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
)



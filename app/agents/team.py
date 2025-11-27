from agno.team import Team

from app.agents.tec_agente import tec_agent



team = Team(
    name="Omarket_Team",
    mode="route",  
    members=[
        tec_agent,
    ],
    instructions=(
        "Este é o time oficial O-Market Data Solutions. "
        "Ele roteia automaticamente perguntas entre os três agentes "
        "especializados (Tecnologia, Estrutura e Consumo). "
        "Cada agente usa RAG estático baseado em PDFs oficiais do catálogo "
        "para garantir respostas concretas e sem alucinação."
    ),
    show_members_responses=False, 
)

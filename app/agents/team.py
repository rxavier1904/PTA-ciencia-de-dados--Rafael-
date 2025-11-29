from agno.team import Team
from agno.models.google import Gemini

from .davi_agent import davi_agent
from .tec_agente import tec_agent
from .agente_casa import agente_casa_agent

team = Team(
    name="O-Market Team",
    mode="route",  
    model=Gemini(id="gemini-2.5-flash"),


    members=[davi_agent, tec_agent, agente_casa_agent],

    instructions="""Você é o Gerente de Inteligência da O-Market.
    Sua missão é ler a pergunta do usuário e decidir qual especialista deve responder.

    ### QUEM FAZ O QUE:
    1. **Agent_Tecnologia_e_Mecanismos (Tec):** - USE PARA: Dúvidas sobre Eletrônicos, Informática, Games, Automotivo.
       - Foco: Hardware e funcionamento técnico.

    2. **Especialista Casa & Conforto (Casa):** <--- ADICIONEI ISSO AQUI
       - USE PARA: Móveis, Cama, Mesa, Banho, Decoração, Utilidades Domésticas, e Construção.
       - Foco: Materiais, dimensões de móveis e conforto.

    3. **Agente de Produtos O-Market (Davi):** - USE PARA: O que sobrar (Moda, Livros, Alimentos, Beleza, Esportes).
       - Foco: Catálogo geral.

    ### REGRAS:
    - Se a pergunta for sobre **conhecimento geral** fora do contexto de produtos, **RECUSE**.
    - Se não tiver certeza, mande para o Agente de Produtos (Davi).
    """,
    show_members_responses=True
)

from agno.team import Team
from agno.models.google import Gemini

# Importa os dois agentes que já estão com a memória carregada
from .davi_agent import davi_agent
from .tec_agente import tec_agent

team = Team(
    name="O-Market Team",
    mode="route", # Modo inteligente que escolhe quem responde
    model=Gemini(id="gemini-2.5-flash"),
    
    # Lista de membros da equipe
    members=[davi_agent, tec_agent],
    
    instructions="""Você é o Gerente de Inteligência da O-Market.
    Sua missão é ler a pergunta do usuário e decidir qual especialista deve responder.

    ### QUEM FAZ O QUE:
    1. **Agent_Tecnologia_e_Mecanismos (Tec):** - USE PARA: Dúvidas sobre Eletrônicos, Informática, Games, Áudio, Automotivo, Eletrodomésticos.
       - Foco: Especificações técnicas, hardware e funcionamento.

    2. **Agente de Produtos O-Market (Davi):** - USE PARA: Dúvidas sobre Moda, Livros, Alimentos, Beleza, Decoração, Esportes.
       - Foco: Catálogo geral e soft-goods.

    ### REGRAS:
    - Se a pergunta for sobre **conhecimento geral** (ex: Capital do Brasil, Receita de Bolo), **RECUSE** responder. Diga que só fala sobre a O-Market.
    - Se não tiver certeza, mande para o Agente de Produtos (Davi).
    """,
    show_members_responses=True
)
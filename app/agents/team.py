from agno.team import Team
from .tec_agente import tec_agent
from agno.models.google import Gemini
from .davi_agent import davi_agent

team = Team(
    name="O-Market Team",
 
    mode="route", 
    
    model=Gemini(id="gemini-2.5-flash"),
    
    members=[davi_agent], 
    
    instructions="""Você é um orquestrador rígido do sistema O-Market.
    
    SUA ÚNICA MISSÃO: Identificar a intenção do usuário e delegar para o 'Agente de Produtos O-Market'.
    
    REGRAS DE OURO:
    1. Você NÃO responde perguntas gerais (como capitais, receitas, clima).
    2. Se a pergunta não for sobre produtos do catálogo, delegue para o agente mesmo assim, para que ELE recuse.
    3. NÃO responda nada por conta própria usando seu conhecimento de treinamento.
    4. Se o usuário perguntar algo fora do contexto (ex: 'Qual a capital do Brasil?'), deixe o agente especializado lidar com a negativa.""",
    
    show_members_responses=True
)

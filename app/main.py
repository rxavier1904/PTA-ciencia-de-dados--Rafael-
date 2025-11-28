from dotenv import load_dotenv

# 1. Carrega variáveis de ambiente (.env) antes de importar qualquer coisa do Agno
# Isso garante que a GOOGLE_API_KEY esteja disponível quando os agentes forem criados.
load_dotenv()

from agno.playground import Playground
from fastapi.responses import HTMLResponse
from fastapi import Request
from urllib.parse import quote

# Importa a equipa que definiste em app/agents/team.py
# Certifica-te que app/agents/__init__.py tem a linha: "from .team import team"
from .agents import team 

# 2. Configuração do Playground
app = Playground(
    name="O-Market Agent Playground",
    description="Ambiente de teste para o Agente de Produtos.",
    teams=[team] # Aqui entra a equipa com o teu agente único opa
).get_app()

# 3. Rota da Home Page (Interface bonita)
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def home(request: Request):
    host = request.url.hostname or "localhost"
    port = request.url.port
    endpoint = f"{host}:{port}" if port else host
    # Gera a URL correta para o Playground na nuvem da Agno
    playground_url = f"https://app.agno.com/playground?endpoint={quote(endpoint)}"

    return f"""
    <!doctype html>
    <html lang="pt-br">
      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>O-Market Agent</title>
        <style>
          :root {{ color-scheme: light dark; }}
          body {{
            font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, "Helvetica Neue", Arial, sans-serif;
            margin: 0; padding: 0; display: grid; min-height: 100dvh; place-items: center;
            background: radial-gradient(1000px 600px at 50% -20%, rgba(99,102,241,.15), transparent);
            color: #1a1a1a;
          }}
          @media (prefers-color-scheme: dark) {{
            body {{ color: #ededed; background: radial-gradient(1000px 600px at 50% -20%, rgba(60, 60, 70,.5), #0f0f0f); }}
          }}
          .card {{
            width: min(680px, 92vw);
            border: 1px solid opacity(12%);
            border-radius: 20px; padding: 40px; 
            backdrop-filter: blur(10px);
            background: rgba(255, 255, 255, 0.05);
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            text-align: center;
          }}
          h1 {{ margin: 0 0 16px; font-size: 32px; font-weight: 700; letter-spacing: -0.02em; }}
          p  {{ margin: 0 0 24px; line-height: 1.6; opacity: .9; font-size: 16px; }}
          a.button {{
            display: inline-block; padding: 14px 24px; border-radius: 50px; text-decoration: none;
            background: #2563eb; color: white; font-weight: 600;
            transition: all 0.2s;
          }}
          a.button:hover {{ background: #1d4ed8; transform: translateY(-2px); box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3); }}
          code {{ background: rgba(100,100,100,0.2); padding: 4px 8px; border-radius: 6px; font-size: 0.9em; }}
        </style>
      </head>
      <body>
        <main class="card">
          <h1>🤖 O-Market AI Agent</h1>
          <p>O seu especialista em catálogo de produtos está pronto.</p>
          
          <div style="margin: 30px 0; padding: 20px; background: rgba(0,0,0,0.2); border-radius: 12px; text-align: left;">
            <p style="margin:0; font-size: 14px; opacity: 0.7; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">Configuração do Playground:</p>
            <p style="margin: 10px 0 0;"><strong>1. Endpoint:</strong> <code>http://{endpoint}/v1</code></p>
            <p style="margin: 5px 0 0;"><strong>2. Agente:</strong> Selecione "Agente de Produtos O-Market"</p>
          </div>

          <a class="button" href="{playground_url}" target="_blank" rel="noopener">Abrir Playground ↗</a>
        </main>
      </body>
    </html>
    """

# 4. Logs de Inicialização
@app.on_event("startup")
async def lifespan():
    host = "127.0.0.1"
    port = "7777"
    endpoint = f"{host}:{port}"
    cloud_url = f"https://app.agno.com/playground?endpoint={quote(endpoint)}"

    print("\n🚀 O-MARKET AGENT INICIADO COM SUCESSO")
    print(f"👉 Acesse localmente: http://{endpoint}")
    print(f"👉 Playground Online: {cloud_url}\n")
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/CITi-UFPE/PTA-ciencia-de-dados">
    <img src="https://ci3.googleusercontent.com/mail-sig/AIorK4zWbC3U-G_vTTZE6rUQqJjzL8u7WNZjzhEaYi9z7slJn8vNhgnFVootxjm377GVCdPGY_F64WolHmGJ" alt="Logo" width="180px">
  </a>

  <h3 align="center">PTA Ciência de Dados</h3>

  <p align="center">
  Este projeto foi criado em 2025.2 com a proposta de trazer a frente de ciência de dados para o Processo de Treinamento de Área (PTA) do CITi. Ele foi desenvolvido com base em práticas modernas de ciência de dados e tem como objetivo capacitar tecnicamente as pessoas aspirantes, alinhando-se às demandas atuais da empresa.
    <br />
    <a href="https://github.com/CITi-UFPE/PTA-ciencia-de-dados"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/CITi-UFPE/PTA-ciencia-de-dados/issues">Report Bug</a>
    ·
    <a href="https://github.com/CITi-UFPE/PTA-ciencia-de-dados/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Tabela de Conteúdo</h2></summary>
  <ol>
    <li><a href="#sobre-o-projeto">Sobre o Projeto</a></li>
    <li><a href="#como-instalar">Como Instalar</a></li>
    <li><a href="#como-rodar">Como Rodar</a></li>
    <li><a href="#contato">Contato</a></li>
  </ol>
</details>

<br/>

## Sobre o Projeto
<br/>

Este projeto foi desenvolvido para o Processo de Treinamento de Área (PTA) do CITi, com foco em ciência de dados. Ele implementa uma arquitetura multiagentes orientada a dados, com componentes para ingestão, processamento e consulta, e expõe funcionalidades por meio de uma API construída com FastAPI. O objetivo principal do projeto é construir uma sistema multiagentes que consegue responder perguntas com base em dados específicos do cliente.



## 1. Visão Geral

O O-Market Data Solutions implementa um **sistema multiagente totalmente local**, baseado em:

- **RAG estático**:
    - Mensagens-base fornecidas pelo usuário
    - PDFs armazenados no repositório
- **Roteador principal** (Especialista PTA O-Market)
- **Três agentes especializados**
- **Ferramentas internas do framework agno** (sem integração externa)


Todo o conhecimento vem exclusivamente de:

1. **Mensagens-base**
2. **Documentos PDF armazenados localmente**

---

# 2. Arquitetura Multiagente

## 2.1. Roteador Principal — Especialista PTA O-Market

(**Derivado das mensagens-base**)

O PTA é o **Master Agent**. Ele:

- Lê **todas as mensagens-base antes de responder**
- Coordena e supervisiona os agentes especializados
- Decide qual agente deve atuar
- Consolida a resposta final
- Mantém coerência com o documento científico do projeto

### Funções principais:

- Interpretar a intenção do usuário
- Roteamento inteligente
- Garantir aderência às normas e conceitos do O-Market
- Explicar quando usa conhecimento geral e não mensagens-base

---

## 2.2. Os Três Agentes Especialistas

### Agent_Tecnologia_e_Mecanismos

**Foco:** desempenho, funcionamento, eficiência, energia

**Responsabilidade:** aspectos mecânicos, computacionais e operacionais

---

### Agent_Estrutura_e_Design

**Foco:** materiais, ergonomia, dimensões, estabilidade

**Responsabilidade:** normas físicas, montagem, materiais, estrutura

---

### Agent_Consumo_e_Estilo

**Foco:** estética, uso, regulamentação de mercado, composição

**Responsabilidade:** aplicação prática, percepção do usuário, composição química

---

# 3. Fontes de Conhecimento

## 3.1. RAG Estático

(**Derivado das mensagens-base e da estrutura do repositório**)

O sistema utiliza:

- **Mensagens-base** — scripts orientadores do O-Market
- **PDFs carregados no diretório** — documentos técnicos adicionais

Características:

- Totalmente local
- Sem consultas externas
- Versionado dentro do repositório
- Utilizado antes do conhecimento geral do modelo

---

# 4. Como Rodar o Sistema

## 4.1. Pré-requisitos

- Python 3.10+
- Biblioteca **agno**
- PDFs e mensagens-base no diretório esperado
- Ambiente Isolado: Abrir o terminal (ou Anaconda Prompt) e criar um ambiente 
virtual.
```
python -m venv agno_env

source agno_env/bin/activate # Linux/Mac
agno_env\Scripts\activate # Windows
```

## 4.2. Estrutura típica do repositório, resumido

```
/o-market/
   /agents/
      agente_casa.py
      davi_agent.py
      tec_agente.py
      team.py
      router.py  
   /pdfs/
   main.py
   README.md

```

---

# 5. Execução

## 5.1. Inicializar do Agente


O Agente:

1. Carrega mensagens-base
2. Carrega PDFs
3. Registra agentes subordinados
4. Inicia sessão interativa

---

# 6. Testes

## 6.1. Testes de Alucinação

- Agente deve sempre usar mensagens-base
- Agentes não podem extrapolar seus domínios

## 6.2. Testes de Roteamento

- Perguntas técnicas → Agent_Tecnologia
- Perguntas estruturais → Agent_Estrutura
- Perguntas de consumo → Agent_Consumo

## 6.3. Testes Integrados

- Agente deve consolidar e explicar decisões
- Cada resposta deve indicar origem do conhecimento
<br/>

## Como Instalar
<br/>

1. Certifique-se de que o **Python** e o **Docker Desktop** estão instalados em sua máquina.

2. Clone o repositório:

   ```sh
   git clone https://github.com/CITi-UFPE/PTA-ciencia-de-dados.git
   ```

3. Entre na pasta do projeto:

   ```sh
   cd PTA-ciencia-de-dados
   ```

<br/>

## Como Rodar

### Usando Docker
<br/>

1. Certifique-se de que o Docker Desktop está em execução.

2. Suba os serviços com o Docker Compose:

   ```sh
   docker-compose up --build
   ```

3. Acesse a aplicação em seu navegador no endereço:

   ```
   http://localhost:7777
   ```

4. Para acessar a documentação interativa da API (Swagger UI), vá para:

   ```
   http://localhost:7777/docs
   ```

<br/>

### Localmente
<br/>

1. Certifique-se de que esteja no diretório principal

2. Instale as dependências: 
    ```
    pip install -r ./requirements.txt
    ```

3. Execute o projeto: 
    ```
    uvicorn app.main:app --port 7777
    ```

4. Acesse a aplicação em seu navegador no endereço:

   ```
   http://localhost:7777
   ```

5. Para acessar a documentação interativa da API (Swagger UI), vá para:

   ```
   http://localhost:7777/docs
   ```

<br/>


## Contato
<br/>

- [CITi UFPE](https://github.com/CITi-UFPE) - contato@citi.org.br
- [João Pedro Bezerra](https://github.com/jpbezera), Líder de Dados em 2025.2 - jpbmtl@cin.ufpe.br


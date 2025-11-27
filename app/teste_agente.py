from app.agents.tec_agente import tec_agent


def main():
    print("\nMessage")
    pergunta = input("> ")

    resp = tec_agent.run(pergunta, search_knowledge=True,
                         return_source_documents=True)

    print("\nResponse\n")
    print(resp.content)

    # Mostrar trechos usados
    if hasattr(resp, "extra_data") and resp.extra_data:
        refs = resp.extra_data.references
        if refs:
            print("\n--- TRECHOS DO PDF UTILIZADOS ---\n")
            for ref in refs:
                for r in ref.references:
                    nome = r.get("name", "desconhecido")
                    meta = r.get("meta_data", {})
                    conteudo = r.get("content", "")

                    preview = conteudo[:200].replace("\n", " ")

                    print(f"[{nome} | page {meta.get('page')}] {preview}\n")


if __name__ == "__main__":
    main()

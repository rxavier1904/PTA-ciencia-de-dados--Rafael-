from dotenv import load_dotenv
load_dotenv()

from app.knowledge.tec_pdf_kb import tec_knowledge


def main():
    print("\nIndexando PDFs de Tecnologia...")

    # Apaga a collection antiga
    tec_knowledge.vector_db.drop()

    # Recria collection
    tec_knowledge.vector_db.create()

    # Indexa PDFs de verdade
    added = tec_knowledge.index()

    print(f"TEC → {added} documentos adicionados")
    print("\nRAG estático atualizado com sucesso!\n")


if __name__ == "__main__":
    main()

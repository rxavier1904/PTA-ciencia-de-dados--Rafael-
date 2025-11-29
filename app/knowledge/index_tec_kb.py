from .tec_pdf_kb import tec_knowledge
import asyncio
from dotenv import load_dotenv
load_dotenv()


async def main():
    print("\nIndexando PDFs de Tecnologia...")

    await tec_knowledge.aload(recreate=True)

    print("\nRAG estático TEC atualizado com sucesso!\n")


if __name__ == "__main__":
    asyncio.run(main())

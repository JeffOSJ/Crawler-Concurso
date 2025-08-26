from domain.concurso import Concurso
from application.filtros import filtrar_concurso
from infraestrutura.telegram_notifier import TelegramNotifier
from infraestrutura.crawler import PCICrawler


import asyncio

if __name__ == "__main__":
    #configurações
    TOKEN = "8460485241:AAGAYTssdBC_JkkeRD4C-Db96ixce-wqtYc"
    CHAT_ID = "5932771233"

    notifier = TelegramNotifier(TOKEN, CHAT_ID)
    crawler = PCICrawler()

    async def main():
        concursos = await crawler.buscar_concursos()
        
        for c in concursos:
            print(c)
            await notifier.enviar(c)


    asyncio.run(main())


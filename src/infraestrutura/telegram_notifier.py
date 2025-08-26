from telegram import Bot


class TelegramNotifier:
    def __init__(self, token, chat_id):
        self.bot = Bot(token=token)
        self.chat_id = chat_id

    async def enviar(self, concurso):
        mensagem = (
            f"📢 Novo Concurso Encontrado!\n"
            f"Área: {concurso.area}\n"
            f"Órgão: {concurso.orgao}\n"
           # f"Título: {concurso.titulo}\n"
            f"Vagas: {concurso.vagas}\n"
            f"Edital: {concurso.link_edital}"
        )
        await self.bot.send_message(chat_id=self.chat_id, text=mensagem)
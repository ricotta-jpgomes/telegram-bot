from telegram.ext import Updater, CommandHandler,MessageHandler, Filters
from handles import start, echo, unknown
from tt_handles import trends


# Chave de acesso a Telegram Bot API. Obtenha a sua aqui: https://t.me/botfather 
TOKEN = ''

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# configurando os dispatchers para lidar com os comandos / mensagens do usuário
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Na linha abaixo eu estou filtrando todas as mensagens recebidas que sejam do tipo texto E não sejam comandos
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo) 
dispatcher.add_handler(echo_handler)

# Controle para obter os trending topics do Twitter (10 primeiros do dia)
trends_handler = CommandHandler('trends', trends)
dispatcher.add_handler(trends_handler)

# controle para caso o bot não encontre nenhum comando correspondente
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
print('listening...')




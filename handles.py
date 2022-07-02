import telegram
from telegram import ChatAction

import time

# mensagem de boas-vindas assim que o bot é ativado
def start(update, context):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

# se a mensagem recebida não corresponder a nenhum comando, o bot repete essa mensagem e pede para que o
# usuário utilize algum comando
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Eu sou um Papagaio = {update.message.text}')
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    time.sleep(1)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Por que você não me manda fazer alguma coisa, {update.effective_user.first_name}? Digite / e veja os comandos disponíveis.')

# se a mensagem recebida for correspondente ao formato de um comando não reconhecido, o bot manda a seguinte mensagem
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Desculpe, comando não identificado. Tente novamente.')
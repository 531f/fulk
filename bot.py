from telegram.ext import Updater
from telegram.ext import CommandHandler

def test(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Fulk funciona! Usa /help para una lista de comandos")

updater = Updater(token='', use_context=True)
dispatcher = updater.dispatcher

test_handler = CommandHandler('test', test)
dispatcher.add_handler(test_handler)

updater.start_polling()

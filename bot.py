from telegram.ext import Updater
from telegram.ext import CommandHandler, 

def test(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Fulk funciona! Usa /help para una lista de comandos")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
    text="Lista de comandos: \n\
        \t/test: Comprueba que el bot funciona\n\
        \t/help: Acabas de usarlo.")

updater = Updater(token='1056678004:AAGTYKJiOHIIxe9At-cf4DiJVEYAMvngQ9A', use_context=True)
dispatcher = updater.dispatcher

test_handler = CommandHandler('test', test)
help_handler = CommandHandler('help', help)
dispatcher.add_handler(test_handler)
dispatcher.add_handler(help_handler)


updater.start_polling()

from telegram.ext import Updater
from telegram.ext import CommandHandler, Filters, MessageHandler
import threading
import time

usertimes_dict = {}
usernames = {}
TIME_TO_DIE = 20
dictLock = threading.Lock()
namesLock = threading.Lock()

class deus_vult(threading.Thread):
    def __init__(self, delay):
        threading.Thread.__init__(self)
        self.delay = delay
    def run(self):
        check_fidelity(self.delay)


def test(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Fulk funciona! Usa /help para una lista de comandos")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
    text="Lista de comandos: \n\
        \t/test: Comprueba que el bot funciona\n\
        \t/help: Acabas de usarlo.")

def check_fidelity(delay):
    while(1):
        time.sleep(delay)
        for user, timeout in usertimes_dict.items():
            if timeout >= TIME_TO_DIE:
                print("INFIDEL!", usernames[user])
            with dictLock:
                usertimes_dict[user] += 1

def pay_our_dues(update,context):

    sender = context.bot.get_chat_member(update.message.chat_id, update.message.from_user.id)
    print("Thou are free {}, for now ".format(sender['user']['username']))
    with namesLock:
        usernames[sender['user']['id']] = sender['user']['username']
    with dictLock:
        usertimes_dict[sender['user']['id']] = 0



updater = Updater(token='', use_context=True)
dispatcher = updater.dispatcher

test_handler = CommandHandler('test', test)
help_handler = CommandHandler('help', help)
tax_handler = MessageHandler(Filters.text, pay_our_dues)
dispatcher.add_handler(test_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(tax_handler)

check = deus_vult(1)

try:
    check.start()
    updater.start_polling()
except KeyboardInterrupt:
    check.join()
    updater.stop()

from google.cloud import storage
from telegram.ext import Dispatcher, CommandHandler, Filters, MessageHandler
from telegram import Update, Bot
import random
from time import sleep
import os

BUCKET_NAME = 'rojaodasicont'
FILE_NAME = 'cont.txt'

storage_client = storage.Client()
bucket = storage_client.bucket(BUCKET_NAME)

def get_count():
    blob = bucket.get_blob(FILE_NAME)
    if blob:
        return int(blob.download_as_text())
    else:
        return 0

def save_count(count):
    blob = bucket.blob(FILE_NAME)
    blob.upload_from_string(str(count))

count = get_count()

def start(bot, update):
    update.message.reply_text("Opa, sou o bot q vai causar absoluto terror no grupo do Dasi com um belo rojão roxo", quote=False)


def acende(bot, update):
    global count
    count += 1
    save_count(count)
    update.message.reply_text("pra", quote=False)
    update.message.reply_text("pra pra", quote=False)
    update.message.reply_text("pra pra pra", quote=False)
    update.message.reply_text("pow", quote=False)
    update.message.reply_text("pow pow", quote=False)
    update.message.reply_text("POW POW POW", quote=False)

def contagem(bot, update):
    global count
    update.message.reply_text(f"O DASI Já usou o Rojão DASIANO {count} vezes")
                         
def webhook(request):
    bot = Bot(token=os.environ["TELEGRAM_TOKEN"])
    
    dispatcher = Dispatcher(bot, None, 0)

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('acende', acende))
    dispatcher.add_handler(CommandHandler('contagem', contagem))
	
    if request.method == 'POST':
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
    return 'ok' 
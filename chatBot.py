#!/usr/bin/python3

import json
import requests
import telegram
import logging
import random

from telegram.ext import Updater, CommandHandler

#Get the Token:
f = open("tok.txt", "r")

TOKEN = f.readline().strip()
f.close()

URL = "https://api.telegram.org/bot{}/".format(TOKEN)

bot = telegram.Bot(token = TOKEN)
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

##################################################################
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hi, I'm a banking helper bot! I make learning about banking quick and easy! Please ask me a question and I'll try my best to answer.")

start_handler = CommandHandler('start', start);
dispatcher.add_handler(start_handler)
    
##################################################################
updater.start_polling()
updater.idle()

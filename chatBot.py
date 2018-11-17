#!/usr/bin/python3

import json
import requests
import telegram
import logging

from telegram.ext import Updater, CommandHandler

#Get the Token:
f = open("tok.txt", "r")
TOKEN = f.readline().strip()
f.close()

URL = "https://api.telegram.org/bot{}/".format(TOKEN)

bot = telegram.Bot(token = TOKEN)
bot = telegram.Bot(TOKEN, True, 4)
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


#Some text:
promos = "Great Question!\n Out current promotions are... "
promo1 = "Open a new savings account and you'll receive 3% interest in the first 3 months! \n For information on how to open an account, go here: \n https://www.rbcroyalbank.com/accounts/savings-accounts.html"
promo2 = "Waive monthly fees for 3 months when you open a new chequing account! \n For information on how to open an account, go here: \n https://www.rbcroyalbank.com/accounts/chequing-accounts.html"
promo3 = "Win an iPad when you Open an All-Inclusive Bank Account!\n Check details here: https://www.rbcroyalbank.com/services/accounts/ipad-offer-f-or.html?utm_campaign=Acct_AppleOffer_All_All_Broad_EN&utm_source=facebook&utm_medium=social&utm_content=na"
promo4 = "Are you a student? Check out our A No-Fee Student Bank Account! It's designed to Save You Money\n https://www.rbcroyalbank.com/accounts/student-banking.html"

banking1 = "Banking is an industry that handles cash, credit, and other financial transactions.\n"
banking2 = "Generally, banking is done by individuals to keep their money safe and help it grow.\n"
banking3 = "Want to know more about banking at RBC? Ask me some questions!"

savings0 = "Saving seems tricky, but here are some ways you can save at RBC:\n"
savings1 = "- Open a TFSA  (Tax-Free savings account)\n"
savings2 = "- Under 18? Look into an RESP account (Registered Education Saving Plan)\n"
savings3 = "- Download our app NOMI to find out where your money goes! This can help you make a budget so you can save some cash."

savings = savings0 + savings1 + savings2 + savings3

confused = "Need clarification on any of the terms above? Ask me \"What's a ___\" and I'll try to help you figure it out!"

#START##########################################################
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hi, I'm a banking helper bot! I make learning about banking quick and easy! Please ask me a question and I'll try my best to answer :) \n Type \'/\' for some quick info!")

start_handler = CommandHandler('start', start);
dispatcher.add_handler(start_handler)
#PROMOTIONS########################################################
def promotions(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text= promos)
    bot.sendMessage(chat_id=update.message.chat_id, text= promo1) #savings account promo
    bot.sendMessage(chat_id=update.message.chat_id, text= promo2) #chequings account promo
    bot.sendMessage(chat_id=update.message.chat_id, text= promo3) #ipad promo
    bot.sendMessage(chat_id=update.message.chat_id, text= promo4) #student accnt promo
    
promo_handler = CommandHandler('promotions', promotions);
dispatcher.add_handler(promo_handler)
#WHAT IS BANKING?##################################################
def whats_banking(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text=banking1)
	bot.sendMessage(chat_id=update.message.chat_id, text=banking2)
	bot.sendMessage(chat_id=update.message.chat_id, text=banking3)

banking_handler = CommandHandler('whats_banking', whats_banking);
dispatcher.add_handler(banking_handler)
#Saving Strategies##################################################
def saving_strats(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text=savings)
	bot.sendMessage(chat_id=update.message.chat_id, text=confused)

savings_handler = CommandHandler('saving_strats', saving_strats);
dispatcher.add_handler(savings_handler)
##################################################################   
def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)
    
##################################################################   
def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            bot_text = m.text
            bot.send_message(chat_id=update.message.chat_id, text= bot_text)   
##################################################################
updater.start_polling()
updater.idle()

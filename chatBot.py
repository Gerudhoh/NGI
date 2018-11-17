#!/usr/bin/python3

#	chatbot.py
#	Developed by Julia Hohenadel

import json
import requests
import telegram
import logging

from telegram.error import NetworkError
from time import sleep
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

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

tfsa = "a TFSA Tax-Free savings account is a saving plan to help you invest."
tfsaPros = "PROS:\n - Account is tax-free"
tfsaCons = "CONS:\n - There's a limit to how much you can add to it a year"

resp = "an RESP is a Registered Education Saving Plan. Generally, your parents or grandparents pay money in it, and while you're still under 18 years old the government matches the money put into the account."
respPros = "PROS:\n - Account is tax-free \n - Government matches money put in"
respCons = "CONS:\n - Only eligible for students under 18 years of age."

credit = "A credit score is a number that represents your overall credit health. It indicates how likely you are to make payments on time or default on a loan."
creditSc = "Higher credit scores mean you have demonstrated responsible credit behavior in the past, which may make potential lenders and creditors more confident when evaluating a request for credit."
creditPitch = "Consider getting one of our RBC credit cards to build your crdit score today!\n https://www.rbcroyalbank.com/credit-cards/all-credit-cards.html#/student"

confused = "Need clarification on any of the terms above? Ask me \"What's a ___\" and I'll try to help you figure it out!"

#MAIN###############################################################


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
	text = update.message.text.lower()
	if text[9:13] == "tfsa":
		bot.sendMessage(chat_id = update.message.chat_id, text = tfsa)
		bot.sendMessage(chat_id = update.message.chat_id, text = tfsaPros)
		bot.sendMessage(chat_id = update.message.chat_id, text = tfsaCons)
	elif text[9:13] == "resp" or text[10:14] == "resp":
		bot.sendMessage(chat_id = update.message.chat_id, text = resp)
		bot.sendMessage(chat_id = update.message.chat_id, text = respPros)
		bot.sendMessage(chat_id = update.message.chat_id, text = respCons)
	elif text[9:26] == "compound interest":
		bot.sendMessage(chat_id = update.message.chat_id, text = cmpInt)
	elif text[9:22] == "credit score":
		bot.sendMessage(chat_id = update.message.chat_id, text = credit)
		bot.sendMessage(chat_id = update.message.chat_id, text = creditSc)
		bot.sendMessage(chat_id = update.message.chat_id, text = creditPitch)
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I don't understand your question :( Remember to type: \"What's a\"...")
		
dispatcher.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()
updater.idle()

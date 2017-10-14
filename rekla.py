import logging
import requests
import polling
import telebot
import time
import eventlet
import botan
import config
import telebot
import os
import flask
from flask import Flask, request
from time import sleep
from telebot import types

server = Flask(__name__)
bot = telebot.TeleBot("458642918:AAGiZ-RhcpvZWGLgOqPvQWwL7fXL2h47lEw")
botan_key = 'c4307719-7cfc-4af1-bf3c-bbf43fb49e7a'

@bot.message_handler(func=lambda message: message.text in ["/about@rickrobot","/about"])
def start(message):
    bot.send_message(message.chat.id,text=("Hey, searching for the best signal channel? Here it is @take_your_profit! You will have 20% profit today!"))

@bot.message_handler(func=lambda message: message.text in ["Hello", "Hello!", "Hi", "Hi!"])
def start(message):
    bot.send_message(message.chat.id,text=("Hey, searching for the best signal channel? Here it is @take_your_profit! You will have 20% profit today!"))


@bot.message_handler(func=lambda message: message.text in ["What is your opinion about all these signal groups?"])
def start(message):
    bot.send_message(message.chat.id,text=("Oh, they are amazing, https://t.me/take_your_profit is my absolute favorite. Making 3-7% daily"))


@bot.message_handler(func=lambda message: message.text in ["Say that","say that"])
def start(message):
    bot.send_message(message.chat.id,text=("Crypto signals based on professional analysis and leaked info from paid groups! Other people pay monthly 0.01-0.08btc to see these calls👎🏻🤢 And YOU have an amazing opportunity to see it all for FREE!💥😎 https://t.me/take_your_profit"))


@server.route("458642918:AAGiZ-RhcpvZWGLgOqPvQWwL7fXL2h47lEw", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("458642918:AAGiZ-RhcpvZWGLgOqPvQWwL7fXL2h47lEw")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://fathomless-ocean-36243.herokuapp.com/458642918:AAGiZ-RhcpvZWGLgOqPvQWwL7fXL2h47lEw")
    return "!", 200



if __name__ == "__main__":
    bot.polling(none_stop=True)

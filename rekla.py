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
from time import sleep
from telebot import types
import requests

url = "https://api.telegram.org/bot458642918:AAGiZ-RhcpvZWGLgOqPvQWwL7fXL2h47lEw/"
bot = telebot.TeleBot("458642918:AAGiZ-RhcpvZWGLgOqPvQWwL7fXL2h47lEw")
botan_key = 'c4307719-7cfc-4af1-bf3c-bbf43fb49e7a'

def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


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

def __init__(self, token):
    self.token = token
    self.api_url = "https://api.telegram.org/bot458642918:AAGiZ-RhcpvZWGLgOqPvQWwL7fXL2h47lEw/".format(token)
    
    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

def send_message(self, chat_id, text):
    params = {'chat_id': chat_id, 'text': text}
    method = 'sendMessage'
    resp = requests.post(self.api_url + method, params)
    return resp
    
    def get_last_update(self):
        get_result = self.get_updates()
        
        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]
        
        return last_update



if __name__ == "__main__":
    bot.polling(none_stop=True)

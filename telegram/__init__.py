# -*- coding: utf-8 -*-

import time
import requests
import logging
import telebot
from time import sleep

USER_API_URL = "https://godville.net/gods/api/bularond/dce5b193b3da"

BOT_TOKEN = '878053869:AAG96xIVJAdYVajscg_RZQc4giVBqEFufIQ'
CHAT_ID = 388003444

SINGLE_RUN = False

bot = telebot.TeleBot(BOT_TOKEN)

old_data, now_data = {}, {}

def update_data():
    global now_data, old_data
    now_data, old_data = requests.get(USER_API_URL).json(), now_data

def gen_new_messeges():
    global now_data, old_data
    messege_form = {
        "level"         : "Я получил новый уровень, теперь {}", 
        "clan_position" : "Мой ранг в гильдии теперь {}",
        "bricks_cnt"    : "Теперь у меня {} кирпичей", 
        "diary_last"    : "{}", 
        "town_name"     : "Я теперь в {}", 
        "quest"         : "Мое задание теперь {}"
                    }
    messages = []
    for key in messege_form.keys():
        if(now_data[key] != old_data[key]):
            messages.append(messege_form[key].format(now_data[key]))
    return messages

def send_messages(messeges):
    for messege in messeges:
        print("Send message", messege)
        bot.send_message(CHAT_ID, messege)
    time.sleep(1)

if __name__ == '__main__':
    update_data()
    sleep(10)
    while True:
        update_data()
        send_messages(gen_new_messeges())
        time.sleep(60)


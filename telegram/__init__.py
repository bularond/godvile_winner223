# -*- coding: utf-8 -*-

import time
import requests
import logging
import telebot
from time import sleep

# Каждый раз получаем по 10 последних записей со стены
USER_API_URL = "https://godville.net/gods/api/bularond/dce5b193b3da"

BOT_TOKEN = '878053869:AAG96xIVJAdYVajscg_RZQc4giVBqEFufIQ'
CHANNEL_NAME = '@godvile_winner223'

# Если True, предполагается использование cron для запуска скрипта
# Если False, процесс запускается и постоянно висит запущенный
SINGLE_RUN = False

bot = telebot.TeleBot(BOT_TOKEN)

true, false, null = True, False, None

old_data, now_data = {}, {"name":"Winner223","godname":"Bularond","gender":"male","level":45,"max_health":276,"inventory_max_num":29,"motto":"Физмат - сила","clan":"Блоги StopGame","clan_position":"советник","alignment":"нейтральный","bricks_cnt":897,"pet":{"pet_name":"Пинки «Пропащий» ❌","pet_class":"огнелис","pet_level":10,"wounded":true},"ark_completed_at":null,"arena_won":33,"arena_lost":28,"health":173,"quest_progress":2,"exp_progress":84,"godpower":77,"gold_approx":"около 3 тысяч","diary_last":"✑ Разобрал монстра на мозаику. За творческий труд забрал 38 золотых.","town_name":"","distance":4,"arena_fight":false,"inventory_num":2,"quest":"пустить по ветру летучий корабль","activatables":[]}

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
    return messege_form

def send_messages(messeges):
    for messege in messeges:
        bot.send_message(CHANNEL_NAME, messege)
    time.sleep(1)

if __name__ == '__main__':
    # Избавляемся от спама в логах от библиотеки requests
    logging.getLogger('requests').setLevel(logging.CRITICAL)
    # Настраиваем наш логгер
    logging.basicConfig(format='[%(asctime)s] %(filename)s:%(lineno)d %(levelname)s - %(message)s', level=logging.INFO,
                        filename='bot_log.log', datefmt='%d.%m.%Y %H:%M:%S')
    while True:
        update_data()
        send_messages(gen_new_messeges())
        # Пауза в 4 минуты перед повторной проверкой
        logging.info('[App] Script went to sleep.')
        time.sleep(60)

    logging.info('[App] Script exited.\n')

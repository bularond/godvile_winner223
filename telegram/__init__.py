# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot("714110486:AAG6qYzhscu2yFy9cDBylNVJSUymC96A040")

@bot.message_handler(content_types=["text"])
def handle_text(message):
    print(message.text)
    bot.send_message(message.from_user.id, "Chenged text")


bot.polling(none_stop = True, interval = 0)

# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass

 # Обработчик для документов и аудиофайлов
@bot.message_handler(content_types=['document', 'audio'])
def handle_document_audio(message):
    pass

bot.polling(none_stop=True, interval=0)

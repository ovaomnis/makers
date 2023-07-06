import random

import telebot
from telebot.types import Message, BotCommand, BotCommandScopeChat


TOKEN = '6179300460:AAED9Om68uFn5QQ5TgaMRWe-KThU7Z_z3NY'

bot = telebot.TeleBot(TOKEN)

# commands = {
#     'play': 'start new game',
#     'start': 'start game'
# }

number = random.randint(1, 99)


@bot.message_handler(commands=['start'])
def start(message: Message):
    global number
    number = random.randint(1, 99)
    bot.send_message(message.chat.id, f"Guess the number between 1 and 99, number is {number}")
    bot.register_next_step_handler_by_chat_id(message.chat.id, is_correct)


def is_correct(message: Message):
    if message.text.isdigit():
        if int(message.text) > number:
            bot.send_message(message.chat.id, f'Too high, number is {number}. Enter another')
            bot.register_next_step_handler_by_chat_id(message.chat.id, is_correct)
        elif int(message.text) < number:
            bot.send_message(message.chat.id, f'Too low, number is {number}. Enter another')
            bot.register_next_step_handler_by_chat_id(message.chat.id, is_correct)
        else:
            bot.send_message(message.chat.id, 'You guessed! /start - to start new game')
    else:
        bot.send_message(message.chat.id, 'Enter number, you stupid idiot')
        bot.register_next_step_handler_by_chat_id(message.chat.id, is_correct)


bot.add_custom_filter(telebot.custom_filters.ChatFilter())
bot.infinity_polling()

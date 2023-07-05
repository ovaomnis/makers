import telebot
import random


API_TOKEN = '6179300460:AAED9Om68uFn5QQ5TgaMRWe-KThU7Z_z3NY'

bot = telebot.TeleBot(API_TOKEN)

stickers = [
    'CAACAgQAAxkBAAEJmFZkpPgFXdMV6bB9jkyS70nHSsiOhAAC6gsAAmwiEVOtWUCotxfPAy8E',
    'CAACAgIAAxkBAAEJmCpkpPeN-xFizAtAxWHAC_Gct5K2cgACoxUAArHj8EiQWIg92f_l1y8E',
    'CAACAgIAAxkBAAEJmCpkpPeN-xFizAtAxWHAC_Gct5K2cgACoxUAArHj8EiQWIg92f_l1y8E',
    'CAACAgIAAxkBAAEJmGFkpPhKMQH-aWul7V4JQ6QYgcUZRgAC-hMAAv0QUUjZsUNnHmt6qy8E',
    'CAACAgIAAxkBAAEJmGVkpPharfMob0C5QGca7gb1V4nmoQACWAwAArC-oEv54CJrXrkjWC8E',
    'CAACAgIAAxkBAAEJmGlkpPhuWAoT4wZ-deO7d-SN1q3UCQAC5g0AAhIioUuD6-gRYxZ6aC8E'
]
#
#
# Content Types -> text, audio, document, photo, video, sticker, animation, geo
# func = lambda message: True -> bot will react to any message
# @bot.message_handler(content_types=['sticker'])
# def star_message(message: telebot.types.Message):
#     bot.send_sticker(message.chat.id, message.sticker.file_id)
#     bot.send_message(message.chat.id, message.sticker.file_id)
#
#
# @bot.message_handler(content_types=['animation'])
# def handle_animation(message: telebot.types.Message):
#     bot.send_animation(message.chat.id, message.animation.file_id)
#     bot.send_message(message.chat.id, message.animation.file_id)


# @bot.message_handler(content_types=)

''' Replay Keyboard MarkUp'''
# keyboard = telebot.types.ReplyKeyboardMarkup()
# button1 = telebot.types.KeyboardButton('Yes')
# button2 = telebot.types.KeyboardButton('No')
# keyboard.add(button1, button2)
#
# start_keyboard = telebot.types.ReplyKeyboardMarkup()
# start = telebot.types.KeyboardButton('Get random sticker')
# start_keyboard.add(start)
#
#
# @bot.message_handler(commands=['start'])
# def option_select(message: telebot.types.Message):
#     bot.send_message(message.chat.id, 'select option', reply_markup=start_keyboard)
#     bot.register_next_step_handler(message, get_random_sticker)
#
#
# def get_random_sticker(message: telebot.types.Message):
#     bot.send_message(message.chat.id, 'Get Random Sticker?', reply_markup=keyboard)
#     bot.register_next_step_handler(message, reply_to_button)
#
#
# def reply_to_button(message: telebot.types.Message):
#     if message.text == 'No':
#         bot.send_message(message.chat.id, 'You will get sticker anyway ))')
#     bot.send_sticker(message.chat.id, random.choice(stickers), reply_markup=start_keyboard)
#     bot.register_next_step_handler(message, option_select)


'''Inline Keyboard MarkUp'''


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton('Да', callback_data='y')
    button2 = telebot.types.InlineKeyboardButton('Нет', callback_data='n')
    keyboard.row(button1, button2)
    bot.send_message(message.chat.id, 'Do you want to get random sticker?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def handler_callback(call: telebot.types.CallbackQuery):
    if call.data == 'n':
        bot.send_message(call.message.chat.id, 'You will get sticker anyway)')
    bot.send_sticker(call.message.chat.id, random.choice(stickers))


bot.polling()

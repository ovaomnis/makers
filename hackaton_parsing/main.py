import datetime
from typing import List

import parser
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

TOKEN = '6333355755:AAHPimpMj0T1EhUwqcKsxScmwC3ZAeAAdLY'
bot = telebot.TeleBot(TOKEN)

news = {}


def get_news() -> dict:
    global news
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    url = f'https://kaktus.media/?lable=8&date={today}&order=popular'
    if not news or news['validated'] < datetime.datetime.now():
        news = {
            'validated': datetime.datetime.now() + datetime.timedelta(seconds=60),
            'news': parser.get_news(parser.get_html(url))
        }
        return news
    return news


@bot.message_handler(commands=['start'])
def start_handler(message: Message):
    news_list = get_news()
    bot.send_message(message.chat.id, '\n'.join([
        f'{news_list["news"].index(n)}. {n["title"]}'
        for n in news_list['news']
    ]))
    bot.send_message(message.chat.id, 'Type number of news')
    bot.register_next_step_handler(message, show_details)


def show_details(message: Message):
    if not (message.text in ['/quit', '/start']):
        if message.text.isdigit():
            news_item = get_news()['news'][int(message.text)]
            keyboard = InlineKeyboardMarkup()
            keyboard.add(
                InlineKeyboardButton('Description', callback_data=message.text),
                InlineKeyboardButton('Select Another', callback_data='another'),
                InlineKeyboardButton('Quit', callback_data='quit'),
                InlineKeyboardButton('List News', callback_data='start')
            )
            bot.send_photo(message.chat.id, news_item['image'], news_item['title'], reply_markup=keyboard)
            # bot.register_callback_query_handler(func=show_description)
        else:
            bot.send_message(message.chat.id, 'Enter number of news. to list news type /start')
            bot.register_next_step_handler(message, show_details)
    else:
        if message.text == '/quit':
            quit_command(message)
        else:
            start_handler(message)


@bot.callback_query_handler(func=lambda call: True)
def show_description(call: CallbackQuery):
    if not(call.data in ['start', 'quit', 'another']):
        news_item = get_news()['news'][int(call.data)]
        bot.send_message(
            call.message.chat.id, parser.get_description(parser.get_html(news_item['link'])),
            reply_markup=InlineKeyboardMarkup().row(
                InlineKeyboardButton('Select Another', callback_data='another'),
                InlineKeyboardButton('Quit', callback_data='quit'),
                InlineKeyboardButton('List News', callback_data='start')
            )
        )
    else:
        if call.data == 'start':
            start_handler(call.message)
        elif call.data == 'quit':
            quit_command(call.message)
        elif call.data == 'another':
            bot.send_message(call.message.chat.id, 'Enter number of news.')
            bot.register_next_step_handler(call.message, show_details)


@bot.message_handler(commands=['quit'])
def quit_command(message: Message):
    bot.send_message(message.chat.id, 'Good Bye')


bot.polling()

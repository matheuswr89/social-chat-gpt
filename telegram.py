import os

import telebot
from dotenv import load_dotenv

from chat import chat

load_dotenv()

bot = telebot.TeleBot(os.environ.get('TELEGRAM_KEY'))
g_messages = []  # group messages
p_messages = []  # private messages


@bot.message_handler(commands=['gpt'])
def group_message(message):
    bot.send_chat_action(chat_id=message.chat.id, action="typing")

    msg = message.text.replace('/gpt ', '')
    g_messages.append(
        {"role": "user", "content": msg})
    reply(message, g_messages)


@bot.message_handler(chat_types=['private'])
def private_message(message):
    bot.send_chat_action(chat_id=message.chat.id, action="typing")

    p_messages.append(
        {"role": "user", "content": message.text})
    reply(message, p_messages)


def reply(message, array):
    response = chat(array)
    bot.reply_to(message, response.choices[0].message.content)


bot.infinity_polling()

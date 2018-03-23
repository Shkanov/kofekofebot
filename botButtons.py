# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 00:21:32 2017

@author: Bulat
"""

# -*- coding: utf-8 -*-

import telebot
from telebot import types
import config
import dbworker
import numpy as np

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def any_msg(message):
    # Создаем клавиатуру и каждую из кнопок (по 2 в ряд)
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    callback_button = types.InlineKeyboardButton(text="Раф", callback_data="Раф")
    callback_button1 = types.InlineKeyboardButton(text="Латте", callback_data="Латте")
    callback_button2 = types.InlineKeyboardButton(text="Мокко", callback_data="Мокко")
    callback_button3 = types.InlineKeyboardButton(text="Эспрессо", callback_data="Эспрессо")
    
    
    
    #switch_button = types.InlineKeyboardButton(text="Switch", switch_inline_query="Telegram")
    keyboard.add(callback_button,callback_button1,callback_button2,callback_button3)
    bot.send_message(message.chat.id, "Какой кофе хочешь?", reply_markup=keyboard)
    dbworker.set_state(message.chat.id, config.States.S_ENTER_KOFE.value)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "Раф":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Твой раф уже готовится!")
            # Уведомление в верхней части экрана
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Раф уже готовится!")
            dbworker.set_state(call.message.chat.id, config.States.S_SET_PAYMENT.value) 
     # Создаем клавиатуру и каждую из кнопок (по 2 в ряд)
     
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            callback_button5 = types.InlineKeyboardButton(text="Наличными", callback_data="Наличными")
            callback_button6 = types.InlineKeyboardButton(text="Переводом", callback_data="Переводом")
            keyboard.add(callback_button5,callback_button6)
            bot.send_message(call.message.chat.id, "Отлично, твой кофе уже готовится! Твой кофе стоит 100 рублей. Твой заказ №"+ str(np.random.randint(1, 10000 + 1)) + "! Ты можешь оплатить наличными либо переводом через Сбербанк Онлайн. Выбери способ оплаты", reply_markup=keyboard)
            dbworker.set_state(call.message.chat.id, config.States.S_START.value)  

        if call.data == "Латте":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Твой латте уже готовится!")
            # Уведомление в верхней части экрана
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Латте уже готовится!")
     
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            callback_button5 = types.InlineKeyboardButton(text="Наличными", callback_data="Наличными")
            callback_button6 = types.InlineKeyboardButton(text="Переводом", callback_data="Переводом")
            keyboard.add(callback_button5,callback_button6)
            bot.send_message(call.message.chat.id, "Отлично, твой кофе уже готовится! Твой кофе стоит 100 рублей. Твой заказ №"+ str(np.random.randint(1, 10000 + 1)) + "! Ты можешь оплатить наличными либо переводом через Сбербанк Онлайн. Выбери способ оплаты", reply_markup=keyboard)
            dbworker.set_state(call.message.chat.id, config.States.S_START.value)  

        if call.data == "Мокко":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Твой мокко уже готовится!")
            # Уведомление в верхней части экрана
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Мокко уже готовится!")
     
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            callback_button5 = types.InlineKeyboardButton(text="Наличными", callback_data="Наличными")
            callback_button6 = types.InlineKeyboardButton(text="Переводом", callback_data="Переводом")
            keyboard.add(callback_button5,callback_button6)
            bot.send_message(call.message.chat.id, "Отлично, твой кофе уже готовится! Твой кофе стоит 100 рублей. Твой заказ №"+ str(np.random.randint(1, 10000 + 1)) + "! Ты можешь оплатить наличными либо переводом через Сбербанк Онлайн. Выбери способ оплаты", reply_markup=keyboard)
            dbworker.set_state(call.message.chat.id, config.States.S_START.value)  

        if call.data == "Эспрессо":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Твой эспрессо уж готовится!")
            # Уведомление в верхней части экрана
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Эспрессо уж готовится!")
     
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            callback_button5 = types.InlineKeyboardButton(text="Наличными", callback_data="Наличными")
            callback_button6 = types.InlineKeyboardButton(text="Переводом", callback_data="Переводом")
            keyboard.add(callback_button5,callback_button6)
            bot.send_message(call.message.chat.id, "Отлично, твой кофе уже готовится! Твой кофе стоит 100 рублей. Твой заказ №"+ str(np.random.randint(1, 10000 + 1)) + "! Ты можешь оплатить наличными либо переводом через Сбербанк Онлайн. Выбери способ оплаты", reply_markup=keyboard)


        if call.data == "Наличными":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Отлично, запомни номер своего заказа! Я тебе напишу, когда кофе будет готов! Если захочешь ещё кофе - пиши!")
            # Уведомление в верхней части экрана
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Готовь бабки!")
        if call.data == "Переводом":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Отлично, номер карты для перевода 5555 5555 5555 5555!При оплате переводом ОБЯЗАТЕЛЬНО напиши в комментариях к переводу номер своего заказа! Я тебе напишу, когда кофе будет готов! Если захочешь ещё кофе - пиши!")
            # Уведомление в верхней части экрана
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Жду бабки!")
            # Если сообщение из инлайн-режима    
    
    
    # Если сообщение из инлайн-режима
    #elif call.inline_message_id:
    #    if call.data == "test":
    #        bot.edit_message_text(inline_message_id=call.inline_message_id, text="Бдыщь")
    #bot.send_message(call.message.chat.id, "Отлично, твой кофе уже готовится! Твой кофе стоит 100 рублей. Твой заказ №"+ str(np.random.randint(1, 10000 + 1)) + "! Ты можешь оплатить наличными либо переводом через Сбербанк Онлайн. Выбери способ оплаты")

          
    
    
"""
# Простейший инлайн-хэндлер для ненулевых запросов
@bot.inline_handler(lambda query: len(query.query) > 0)
def query_text(query):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="test"))
    results = []
    # Обратите внимание: вместо текста - объект input_message_content c текстом!
    single_msg = types.InlineQueryResultArticle(
        id="1", title="Press me",
        input_message_content=types.InputTextMessageContent(message_text="Я – сообщение из инлайн-режима"),
        reply_markup=kb
    )
    results.append(single_msg)
    bot.answer_inline_query(query.id, results)
"""
if __name__ == '__main__':
    try:

        bot.polling(none_stop=True)

        # ConnectionError and ReadTimeout because of possible timout of the requests library

        # TypeError for moviepy errors

        # maybe there are others, therefore Exception

    except Exception as e:

        print(e)

        time.sleep(30)
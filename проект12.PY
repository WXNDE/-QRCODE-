from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import qrcode
from io import BytesIO
from aiogram import Bot, Dispatcher, types, executor
import telebot
from telebot import types
token=''
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['input'])
def send_qr(message):
    random_data = 'проходвшколумонаховадианаденисовна'
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(random_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    bot.send_photo(message.chat.id, img_io)
@bot.message_handler(commands=['output'])
def send_qr(message):
    random_data = 'выходвшколумонаховадианаденисовна'
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(random_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    bot.send_photo(message.chat.id, img_io)
@bot.message_handler(commands=['start'])
def handle_start(message):

  keyboard = types.ReplyKeyboardMarkup(row_width=2)
  button1 = types.KeyboardButton('Вход в Систему')
  button2 = types.KeyboardButton('Тех.поддержка')
  keyboard.add(button1, button2)


  bot.reply_to(message, 'Добро пожаловать в нашу систему! Войди в свой личный аккаунт и получишь QR-code для сегодняшнего прохода в школу!', reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
  if message.text == 'Вход в Систему':
      bot.reply_to(message, 'Отправь свой логин и пароль для входа в систему.')
  elif message.text == 'Тех.поддержка':
      bot.reply_to(message, 'Напиши с какой проблемой столкнулся и мы вскоре тебе ответим!')
  else:
        if message.text == 'monahovadianadenisovna and sGhjk_152':
            bot.reply_to(message, 'Ты зашла в свой личный аккаунт. Открыт доступ к получению QR-code.')
        if message.text == 'egorkyrihinvladymirovich and 23032007':
            bot.reply_to(message, 'Ты зашел в свой личный аккаунт. Открыт доступ к получению QR-code.')



bot.infinity_polling()

import random
from datetime import date

import config
from telebot import types
import telebot
from db import Roles, Users
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///users.db',echo=True, connect_args={"check_same_thread": False})
session = Session(bind=engine)

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start(mes: types.Message):
    bot.send_message(mes.chat.id, 'Вы в главном меню', reply_markup=config.markup)


@bot.message_handler(content_types=['text'])
def pushButton(mes: types.Message):
    if mes.text == 'Записать работника':
        mesFullName = bot.send_message(mes.chat.id, 'Введите ФИО работника', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(mesFullName, recordEmployee)


def recordEmployee(mes: types.Message):
    user = Users(
        id = random.randint(1,999999999),
        fio = mes.text,
        datar=date.fromordinal(random.randint(
            date.today().replace(day=1, month=1, year=2020).toordinal(),
            date.today().toordinal())),
        id_role = random.randint(1, 2)
    )
    session.add(user)
    session.commit()

    bot.send_message(mes.chat.id, "Работник успешно добавлен", reply_markup=config.markup)


if __name__ == '__main__':
    bot.infinity_polling()

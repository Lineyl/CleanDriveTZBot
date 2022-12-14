import random
from datetime import date
import sqlite3
import xlsxwriter

import config
from telebot import types
import telebot
from db import Roles, Users
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///users.db',echo=True, connect_args={"check_same_thread": False})
session = Session(bind=engine)

con = sqlite3.connect('users.db', check_same_thread=False)
cur = con.cursor()

bot = telebot.TeleBot(config.token)




@bot.message_handler(commands=['start'])
def start(mes: types.Message):
    bot.send_message(mes.chat.id, 'Вы в главном меню', reply_markup=config.markup)

@bot.message_handler(content_types=['text'])
def pushButton(mes: types.Message):
    if mes.text == 'Записать работника':
        mesFullName = bot.send_message(mes.chat.id, 'Введите ФИО работника', reply_markup=config.cancel)
        bot.register_next_step_handler(mesFullName, recordEmployee)


def recordEmployee(mes: types.Message):
    if mes.text == 'Отмена':
        bot.send_message(mes.chat.id, "Действие отменено", reply_markup=config.markup)
        return
    user = Users(
        id = random.randint(1,999999999),
        fio = mes.text,
        datar=date.fromordinal(random.randint(
            date.today().replace(day=1, month=1, year=1950).toordinal(),
            date.today().replace(year=2002).toordinal())),
        id_role = random.randint(1, 2)
    )
    session.add(user)
    session.commit()

    count = len(cur.execute('SELECT * FROM users').fetchall())
    data = cur.execute(
        f'SELECT fio, datar, name FROM users JOIN roles ON users.id_role=roles.id LIMIT {count - 5}, {count - 1} ').fetchall()

    workbook = xlsxwriter.Workbook('Employee.xlsx')
    sheet = workbook.add_worksheet('Users')

    sheet.set_column(0, 3, 30)
    cell_format = workbook.add_format()
    cell_format.set_bg_color('#DCDCDC')
    cell_format.set_font_size(18)

    row = 1
    col = 0
    for i in range(len(config.tableHeader)):
        sheet.write(0, col, config.tableHeader[i], cell_format)
        for j in range(len(data)):
            sheet.write(row, col, data[j][i])
            row+=1
        row=1
        col+=1

    workbook.close()

    with open('Employee.xlsx','rb') as doc:
        bot.send_document(mes.chat.id, doc, caption='Работник успешно добавлен')
    bot.send_message(mes.chat.id, "Главное меню", reply_markup=config.markup)


if __name__ == '__main__':
    bot.infinity_polling()

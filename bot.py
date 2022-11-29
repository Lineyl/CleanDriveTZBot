import config
from telebot import types
import telebot


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start(mes: types.Message):
    bot.send_message(mes.chat.id, 'Вы в главном меню', reply_markup=config.markup)


@bot.message_handler(content_types=['text'])
def pushButton(mes: types.Message):
    if mes.text == 'Записать работника':
        mesFullName = bot.send_message(mes.chat.id, 'Введите ФИО работника', reply_markup= types.ReplyKeyboardRemove())
        bot.register_next_step_handler(mesFullName, recordEmployee)


def recordEmployee(mes):
    bot.send_message(mes.chat.id, "Работник успешно добавлен", reply_markup=config.markup)




if __name__ == '__main__':
    bot.infinity_polling()

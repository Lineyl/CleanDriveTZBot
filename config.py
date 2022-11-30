from telebot import types
# from telebot.handler_backends import State, StatesGroup

tableHeader = ['ФИО', 'Дата рождения', 'Наименование роли']

token = '5944247071:AAGYlecrUsmV1o7wDRCLUo0kAQqg2VMwq5U'

markup = types.ReplyKeyboardMarkup(
    resize_keyboard=True).add(
    types.KeyboardButton("Записать работника"))
cancel = types.ReplyKeyboardMarkup(
    resize_keyboard=True).add(
    types.KeyboardButton("Отмена"))


# class RecordEmployee(StatesGroup):
#     recordFullName = State()

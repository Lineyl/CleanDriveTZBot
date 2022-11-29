from telebot import types
# from telebot.handler_backends import State, StatesGroup

token = '5944247071:AAGYlecrUsmV1o7wDRCLUo0kAQqg2VMwq5U'

markup = types.ReplyKeyboardMarkup(
    resize_keyboard=True).add(
    types.KeyboardButton("Записать работника"))


# class RecordEmployee(StatesGroup):
#     recordFullName = State()

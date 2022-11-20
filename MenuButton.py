from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


BtnWorkHrs = KeyboardButton('/work_hours')
BtnAskQuestion = KeyboardButton('/question')
#ButtonMain = KeyboardButton('В начало')
menuBtns = ReplyKeyboardMarkup(resize_keyboard=True)

menuBtns.row(BtnWorkHrs, BtnAskQuestion)

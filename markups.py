from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



btnProfile = KeyboardButton('Profil')
btnSub = KeyboardButton("Kurslar")

mainMenu = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu.add(btnProfile, btnSub)
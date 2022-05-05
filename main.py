import telebot
from telebot import types
from string import Template
from db import Database


TOKEN = "5394556613:AAFfqceoE2ukKxXHEqvhFc_vwnLuNqam2wU"
bot = telebot.TeleBot(TOKEN, parse_mode = False)
db = Database("db.db")

user_dict = {}

class User:
    def __init__(self, city) -> None:
        self.city = city
        keys = ["full_name", "phone", "birth_date", "address"]

        for key in keys:
            self.key = None
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if (not db.user_exists(message.from_user.id)):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton('📔Biz haqimizda',)
        item2 = types.KeyboardButton('🗂Kurslar')
        item3 = types.KeyboardButton('📑Ro\'yxatdan o\'tish')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, "Salom "+ message.from_user.first_name + ", Botimizga xush kelibsiz. Quyidagilardan birini tanlang", reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton('📔Biz haqimizda',)
        item2 = types.KeyboardButton('🗂Kurslar')
        item3 = types.KeyboardButton('👨‍🎓Profil')
        item4 = types.KeyboardButton('💵To\'lov qilish')
        markup.add(item1, item2, item3,item4)
        bot.send_message(message.chat.id,"Assalomu alaykum", reply_markup=markup)
@bot.message_handler(content_types=["text"])
def func(message):
    if message.chat.type == "private":
        if message.text =="📔Biz haqimizda":
            bot.send_message(message.chat.id, "Biz haqimizda .....")
        elif message.text == "🗂Kurslar":

            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('🧩Lego Mindstorms EV3',)
            item2 = types.KeyboardButton('💡Arduino STEM EDU')
            item3 = types.KeyboardButton('🧩Lego Spike')
            item4 = types.KeyboardButton('🏎BBC Micro:bit')
            item5 = types.KeyboardButton('⚙️Calliope mini')
            item6 = types.KeyboardButton('🤖Makeblock mBot')
            item7 = types.KeyboardButton('Orqaga qaytish')
            markup2.add(item1, item2, item3,item4, item5, item6,item7)

            msg = bot.send_message(message.chat.id, "Kurs haqida ma'lumot olish uchun uning ustiga bosing", reply_markup=markup2)
            bot.register_next_step_handler(msg,Kurslar)
        elif message.text =="📑Ro\'yxatdan o\'tish":
            db.add_user(message.chat.id)
            markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton('Bektemir tumani',)
            item2 = types.KeyboardButton('Chilonzor tumani')
            item3 = types.KeyboardButton('Yashnobod tumani')
            item4 = types.KeyboardButton('Mirobod tumani')
            item5 = types.KeyboardButton('Mirzo Ulugʻbek tumani')
            item6 = types.KeyboardButton('Sergeli tumani')
            item7 = types.KeyboardButton('Shayxontohur tumani',)
            item8 = types.KeyboardButton('Olmazor tumani')
            item9 = types.KeyboardButton('Uchtepa tumani')
            item10 = types.KeyboardButton('Yakkasaroy tumani')
            item11 = types.KeyboardButton('Yunusobod tumani')
            item12 = types.KeyboardButton('Yangihayot tumani')
            markup3.add(item1, item2, item3,item4, item5, item6,item7,item8, item9, item10,item11, item12,)
            msg = bot.send_message(message.chat.id, "🌆Shahringiz?", reply_markup=markup3)
            bot.register_next_step_handler(msg,proccess_city_step)
        elif message.text=="👨‍🎓Profil":
            bot.send_message(message.chat.id, str(db.get_user(message.chat.id)))
def Kurslar(message):
    if message.chat.type=="private":
        if message.text=="Orqaga qaytish":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('📔Biz haqimizda',)
            item2 = types.KeyboardButton('🗂Kurslar')
            item3 = types.KeyboardButton('📑Ro\'yxatdan o\'tish')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, "Bosh menu", reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item = types.KeyboardButton("Orqaga qaytish")
            markup.add(item)
            msg = bot.send_message(message.chat.id,"Hali bitmagan...",reply_markup=markup)
            bot.register_next_step_handler(msg,Kurslar)
def proccess_city_step(message):
    try:
        chat_id= message.chat.id
        user_dict[chat_id]= User(message.text)
        db.set_address(message.chat.id,message.text)
        markup = types.ReplyKeyboardRemove(selective=False)
        msg = bot.send_message(chat_id, "📄Ism Sharifingizni kiriting\n\nMisol uchun\nTeshaboy Qo'ziyev", reply_markup=markup)
        bot.register_next_step_handler(msg,proccess_full_name_step)
    except:
        bot.reply_to(message, "ooops!!")
def proccess_full_name_step(message):
    try:
        chat_id= message.chat.id
        user = user_dict[chat_id]
        user.full_name = message.text
        db.set_firstname(message.chat.id,message.text)
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        btn_phone = types.KeyboardButton(text="☎️Telefon raqamimni yuborish",request_contact=True)
        keyboard.add(btn_phone)
        msg = bot.send_message(chat_id, "📞Telefon raqamingiz",reply_markup=keyboard)
        bot.register_next_step_handler(msg,proccess_phone_number_step)
    except:
        bot.reply_to(message, "ooops!!")
def proccess_phone_number_step(message):
    try:
        chat_id= message.chat.id
        user = user_dict[chat_id]
        user.phone = message.contact.phone_number
        db.set_phone(message.chat.id,user.phone)
        markup = types.ReplyKeyboardRemove(selective=False)
        msg = bot.send_message(chat_id, "📅Tug'ilgan sanangizni kiriting\n\nFormat:<b>DD/MM/YYYY</b>",parse_mode="HTML",reply_markup=markup)
        bot.register_next_step_handler(msg,proccess_birth_date_step)
    except:
        bot.reply_to(message, "ooops!!")
def proccess_birth_date_step(message):
    try:
        chat_id= message.chat.id
        user = user_dict[chat_id]
        user.birth_date = message.text
        db.set_birth(message.chat.id,user.birth_date)
        bot.send_message(chat_id, getregdata(user,"Sizning ma'lumotlaringiz",message.from_user.first_name),parse_mode="HTML")
        bot.send_message(-1001719418514, getregdata(user,"Yangi ma'lumot",bot.get_me().username),parse_mode="HTML")
    except:
        bot.reply_to(message, "ooops!!")
def getregdata(user,title,name):
    t = Template("$title <b>$name</b> \nShahar: <b>$userCity</b>\nFIO: <b>$Fullname</b>\nPhone: <b>$Phone</b>\nBirth_date: <b>$Birth_date</b> \nIltimos /start buyrugini yuboring")
    return t.substitute({
        'title':title,
        'name':name,
        'userCity':user.city,
        'Fullname':user.full_name,
        'Phone':user.phone,
        'Birth_date':user.birth_date,
    })
bot.infinity_polling()
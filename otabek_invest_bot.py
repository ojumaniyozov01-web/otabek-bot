"""
Otabek Invest — Telegram Bot
"""

import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

TELEGRAM_CHANNEL = "https://t.me/otabek_investuzb"
YOUTUBE_CHANNEL  = "https://www.youtube.com/@otabek_invest"
ADMIN_CONTACT    = "https://t.me/Rus1amovich_01"
PAYNET_LINK      = "https://app.paynet.uz/qr-online/00020101021140440012qr-online.uz01186r0pXuqltFgF3f8Awg0202115204531153038605802UZ5910AO'PAYNET'6008Tashkent610610002164280002uz0106PAYNET0208Toshkent80520012qr-online.uz03097120207070419marketing@paynet.uz6304A4CF"

VIDEO_MENTORSHIP = "https://youtu.be/PT8I9SWUb4c"
VIDEO_TRADING    = "https://youtu.be/KRVZ6M-_GQY"

def main_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        KeyboardButton("👤 Men haqimda"),
        KeyboardButton("📢 Telegram kanal"),
        KeyboardButton("🎥 YouTube kanal"),
        KeyboardButton("📈 Trading haqida"),
        KeyboardButton("🎓 Mentorship"),
        KeyboardButton("🏆 O'quvchilar natijalari"),
        KeyboardButton("📩 Admin bilan aloqa"),
    )
    return markup

def back_keyboard():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🏠 Bosh menyu", callback_data="home"))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    text = (
        "Assalomu alaykum! 👋\n\n"
        "Otabek Invest botiga xush kelibsiz!\n\n"
        "Quyidagi bo'limlardan birini tanlang 👇"
    )
    bot.send_message(message.chat.id, text, reply_markup=main_keyboard())

@bot.message_handler(func=lambda msg: msg.text == "👤 Men haqimda")
def about_me(message):
    text = (
        "👤 Men haqimda\n\n"
        "Salom! Men Otabek — professional trader.\n\n"
        "📅 2022-yilda valyuta bozorini o'rganishni boshlaganman\n"
        "💱 Valyuta bozorida (Forex) savdo qilaman\n"
        "👥 30 ga yaqin shogirdlarim bor\n"
        "📊 Prop hisob va real hisobda savdo qilaman\n"
        "⏳ Bu soha bilan professional shug'ullanishni boshlaganimga 1.5 yil bo'ldi\n\n"
        "Savollaringiz bo'lsa, admin bilan bog'laning! 👇"
    )
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📩 Admin bilan bog'lanish", url=ADMIN_CONTACT))
    markup.add(InlineKeyboardButton("🏠 Bosh menyu", callback_data="home"))
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text == "📢 Telegram kanal")
def tg_channel(message):
    text = (
        "📢 Telegram kanal\n\n"
        "Kanalimizda har kuni:\n\n"
        "📊 Bozor tahlili\n"
        "📌 Foydali signallar\n"
        "🎓 O'quv materiallari\n"
        "💡 Trading sirlari\n\n"
        "Kanalga qo'shiling va bilimlaringizni oshiring! 👇"
    )
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📢 Kanalga o'tish", url=TELEGRAM_CHANNEL))
    markup.add(InlineKeyboardButton("🏠 Bosh menyu", callback_data="home"))
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text == "🎥 YouTube kanal")
def yt_channel(message):
    text = (
        "🎥 YouTube kanal\n\n"
        "YouTube kanalimizda:\n\n"
        "🎓 Bepul darsliklar\n"
        "📊 Bozor tahlillari\n"
        "📈 Trading strategiyalari\n"
        "💡 Foydali maslahatlar\n\n"
        "Kanalga obuna bo'ling! 👇"
    )
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🎥 YouTube kanalga o'tish", url=YOUTUBE_CHANNEL))
    markup.add(InlineKeyboardButton("🏠 Bosh menyu", callback_data="home"))
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text == "📈 Trading haqida")
def trading_info(message):
    text = (
        "📈 Trading haqida\n\n"
        "Trading — bu moliyaviy bozorlarda savdo qilish orqali daromad topish.\n\n"
        "Men o'rgatadigan yo'nalishlar:\n\n"
        "💱 Valyuta bozori (Forex)\n"
        "📊 Texnik tahlil\n"
        "🛡 Risk menejment\n"
        "📉 Grafik o'qish\n\n"
        "Batafsil ma'lumot uchun videoni ko'ring! 👇"
    )
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🎬 Videoni ko'rish", url=VIDEO_TRADING))
    markup.add(InlineKeyboardButton("🏠 Bosh menyu", callback_data="home"))
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text == "🎓 Mentorship")
def mentorship(message):
    text = (
        "🎓 Mentorship dasturi\n\n"
        "Mentorship — bu men bilan individual ishlash imkoniyati.\n\n"
        "Dasturga nima kiradi:\n\n"
        "✅ Shaxsiy dars jadvali\n"
        "✅ Amaliy mashg'ulotlar\n"
        "✅ 24/7 savollarga javob\n"
        "✅ Real bozorda amaliyot\n"
        "✅ Prop hisob bo'yicha yo'riqnoma\n\n"
        "Narxlar:\n\n"
        "💻 Online — 169$\n"
        "🏫 Offline — 399$\n\n"
        "Qaysi formatni tanlaysiz? 👇"
    )
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🎬 Videoni ko'rish", url=VIDEO_MENTORSHIP))
    markup.add(InlineKeyboardButton("💻 Online — 169$", callback_data="join_online"))
    markup.add(InlineKeyboardButton("🏫 Offline — 399$", callback_data="join_offline"))
    markup.add(InlineKeyboardButton("🏠 Bosh menyu", callback_data="home"))
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "join_online")
def join_online(call):
    text = (
        "💻 Online mentorship — 169$\n\n"
        "To'lov qilish uchun quyidagi tugmani bosing.\n\n"
        "To'lovdan so'ng chekni adminga yuboring —\n"
        "sizni dasturga qo'shamiz! 👇"
    )
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("💳 Paynet orqali to'lash", url=PAYNET_LINK))
    markup.add(InlineKeyboardButton("📩 Chekni adminga yuborish", url=ADMIN_CONTACT))
    markup.add(InlineKeyboardButton("🏠 Bosh menyu", callback_data="home"))
    bot.send_message(call.message.chat.id, text, reply_markup=markup)
    bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=lambda call: call.data == "join_offline")
def join_offline(call):
    text = (
        "🏫 Offline mentorship — 399$\n\n"
        "To'lov qilish uchun quyidagi tugmani bosing.\n\n"
        "To'lovdan so'ng chekni adminga yuboring —\n"
        "sizni dasturga qo'shamiz! 👇"
    )
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("💳 Paynet orqali to'lash", url=PAYNET_LINK))
    markup.add(InlineKeyboardButton("📩 Chekni adminga yuborish", url=ADMIN_CONTACT))
    markup.add(InlineKeyboardButton("🏠 Bosh menyu", callback_data="home"))
    bot.send_message(call.message.chat.id, text, reply_markup=markup)
    bot.answer_callback_query(call.id)

@bot.message_handler(func=lambda msg: msg.text == "🏆 O'quvchilar natijalari")
def results(message):
    text = (
        "🏆 O'quvchilar natijalari\n\n"
        "Mening o'quvchilarimning real natijalari:\n\n"
        "👥 30 ga yaqin o'quvchi\n"
        "💰 Ko'pchilik doimiy daromad olmoqda\n"
        "🌍 O'zbekistonning turli shaharlaridan o'quvchilar\n"
        "📊 Prop hisob va real hisobda savdo qiluvchilar\n\n"
        "Siz ham qo'shiling! 👇"
    )
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📢 Telegram kanal", url=TELEGRAM_CHANNEL))
    markup.add(InlineKeyboardButton("📩 Admin bilan bog'lanish", url=ADMIN_CONTACT))
    markup.add(InlineKeyboardButton("🏠 Bosh menyu", callback_data="home"))
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text == "📩 Admin bilan aloqa")
def admin_contact(message):
    text = (
        "📩 Admin bilan aloqa\n\n"
        "Savol yoki takliflaringiz bo'lsa,\n"
        "admin bilan bog'laning!\n\n"
        "Tez orada javob beramiz 👇"
    )
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📩 Admin bilan yozish", url=ADMIN_CONTACT))
    markup.add(InlineKeyboardButton("🏠 Bosh menyu", callback_data="home"))
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "home")
def go_home(call):
    text = (
        "🏠 Bosh menyu\n\n"
        "Quyidagi bo'limlardan birini tanlang 👇"
    )
    bot.send_message(call.message.chat.id, text, reply_markup=main_keyboard())
    bot.answer_callback_query(call.id)

@bot.message_handler(func=lambda msg: True)
def unknown(message):
    bot.send_message(message.chat.id, "Quyidagi tugmalardan birini tanlang 👇", reply_markup=main_keyboard())

if __name__ == "__main__":
    print("Otabek Invest boti ishga tushdi...")
    print("Toxtatish uchun: Ctrl+C")
    bot.infinity_polling()

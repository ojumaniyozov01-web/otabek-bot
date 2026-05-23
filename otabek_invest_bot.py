"""
Otabek Invest — Telegram Bot
==============================
O'rnatish:
  pip install pytelegrambotapi

Ishga tushirish:
  python otabek_invest_bot.py
"""

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# =============================================
#  TOKEN
# =============================================
BOT_TOKEN = "8997085031:AAFjdTSLJENiisPTF6oNN8erUhhy8rfIcsI"

bot = telebot.TeleBot(BOT_TOKEN)

# =============================================
#  MA'LUMOTLAR — o'zingizga mos o'zgartiring
# =============================================

# Kanallar
TELEGRAM_CHANNEL = "https://t.me/otabek_investuzb"
YOUTUBE_CHANNEL  = "https://www.youtube.com/@otabek_invest"

# Videolar (YouTube linki)
VIDEO_MENTORSHIP = "https://youtu.be/PT8I9SWUb4c"
VIDEO_TRADING    = "https://youtu.be/KRVZ6M-_GQY"
VIDEO_ABOUT_ME   = ""   # Tayyor bo'lganda shu yerga qo'ying
VIDEO_TG_CHANNEL = ""   # Tayyor bo'lganda shu yerga qo'ying
VIDEO_NATIJALAR  = ""   # Tayyor bo'lganda shu yerga qo'ying

# Xush kelibsiz matni
WELCOME_TEXT = (
    "Assalomu alaykum! 👋\n\n"
    "Men *Otabek* — trader va mentor.\n\n"
    "Quyidagi bo'limlardan birini tanlang 👇"
)

# =============================================
#  ASOSIY KLAVIATURA
# =============================================
def main_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        KeyboardButton("👤 Men haqimda"),
        KeyboardButton("📢 Telegram kanal"),
        KeyboardButton("🎥 YouTube kanal"),
        KeyboardButton("📈 Trading haqida"),
        KeyboardButton("🎓 Mentorship"),
        KeyboardButton("🏆 O'quvchilar natijalari"),
    )
    return markup

# =============================================
#  ORQAGA QAYTISH TUGMASI
# =============================================
def back_keyboard():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🏠 Bosh menyu", callback_data="home"))
    return markup

# =============================================
#  /start
# =============================================
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        WELCOME_TEXT,
        parse_mode="Markdown",
        reply_markup=main_keyboard()
    )

# =============================================
#  TUGMALAR
# =============================================
@bot.message_handler(func=lambda msg: msg.text == "👤 Men haqimda")
def about_me(message):
    text = (
        "👤 *Men haqimda*\n\n"
        "Men Otabek — professional trader va mentor.\n"
        "Trading bilan 2018-yildan beri shug'ullanaman.\n\n"
        "📈 Forex, Crypto va fond bozorida tajribam bor.\n"
        "🎓 100+ o'quvchiga trading o'rgatganman.\n\n"
        "📌 Videoni tez orada qo'shaman!"
    )
    if VIDEO_ABOUT_ME:
        text += f"\n\n🎬 [Videoni ko'rish]({VIDEO_ABOUT_ME})"
        bot.send_message(message.chat.id, text, parse_mode="Markdown",
                         reply_markup=back_keyboard(), disable_web_page_preview=False)
    else:
        bot.send_message(message.chat.id, text, parse_mode="Markdown",
                         reply_markup=back_keyboard())


@bot.message_handler(func=lambda msg: msg.text == "📢 Telegram kanal")
def tg_channel(message):
    text = (
        "📢 *Telegram kanal*\n\n"
        "Kanalimizda har kuni:\n"
        "• 📊 Bozor tahlili\n"
        "• 📌 Foydali signallar\n"
        "• 🎓 O'quv materiallari\n\n"
        f"👉 Kanalga o'tish: {TELEGRAM_CHANNEL}"
    )
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📢 Kanalga o'tish", url=TELEGRAM_CHANNEL))
    markup.add(InlineKeyboardButton("🏠 Bosh menyu", callback_data="home"))

    if VIDEO_TG_CHANNEL:
        bot.send_message(message.chat.id,
                         text + f"\n\n🎬 [Kanal haqida video]({VIDEO_TG_CHANNEL})",
                         parse_mode="Markdown", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(func=lambda msg: msg.text == "🎥 YouTube kanal")
def yt_channel(message):
    text = (
        "🎥 *YouTube kanal*\n\n"
        "YouTube kanalimizda:\n"
        "• 🎓 Bepul darsliklar\n"
        "• 📊 Tahlillar va strategiyalar\n"
        "• 💡 Trading sirlari\n\n"
        f"👉 Kanalga o'tish: {YOUTUBE_CHANNEL}"
    )
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🎥 YouTube kanalga o'tish", url=YOUTUBE_CHANNEL))
    markup.add(InlineKeyboardButton("🏠 Bosh menyu", callback_data="home"))
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(func=lambda msg: msg.text == "📈 Trading haqida")
def trading_info(message):
    text = (
        "📈 *Trading haqida*\n\n"
        "Trading — bu moliyaviy bozorlarda savdo qilish orqali daromad topish.\n\n"
        "📌 Men o'rgatadigan yo'nalishlar:\n"
        "• Forex bozori\n"
        "• Kripto bozori\n"
        "• Texnik tahlil\n"
        "• Risk menejment\n\n"
        "🎬 Quyidagi videoda batafsil ma'lumot:"
    )
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🎬 Videoni ko'rish", url=VIDEO_TRADING))
    markup.add(InlineKeyboardButton("🏠 Bosh menyu", callback_data="home"))
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(func=lambda msg: msg.text == "🎓 Mentorship")
def mentorship(message):
    text = (
        "🎓 *Mentorship dasturi*\n\n"
        "Mentorship — bu men bilan individual ishlash imkoniyati.\n\n"
        "✅ Dasturga nima kiradi:\n"
        "• Shaxsiy dars jadvali\n"
        "• Amaliy mashg'ulotlar\n"
        "• 24/7 savollarga javob\n"
        "• Real bozorda amaliyot\n\n"
        "🎬 Quyidagi videoda batafsil ma'lumot:"
    )
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🎬 Videoni ko'rish", url=VIDEO_MENTORSHIP))
    markup.add(InlineKeyboardButton("📢 Bog'lanish", url=TELEGRAM_CHANNEL))
    markup.add(InlineKeyboardButton("🏠 Bosh menyu", callback_data="home"))
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(func=lambda msg: msg.text == "🏆 O'quvchilar natijalari")
def results(message):
    text = (
        "🏆 *O'quvchilar natijalari*\n\n"
        "Mening o'quvchilarimning real natijalari:\n\n"
        "📊 100+ o'quvchi\n"
        "💰 Ko'pchilik doimiy daromad olmoqda\n"
        "🌍 O'zbekiston va chet eldan o'quvchilar\n\n"
        "📌 Natijalar rasmlari va videolari tez orada qo'shiladi!\n\n"
        "👉 Ko'proq ma'lumot uchun kanalga o'ting:"
    )
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📢 Telegram kanal", url=TELEGRAM_CHANNEL))
    markup.add(InlineKeyboardButton("🏠 Bosh menyu", callback_data="home"))
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


# =============================================
#  INLINE CALLBACK — Bosh menyu
# =============================================
@bot.callback_query_handler(func=lambda call: call.data == "home")
def go_home(call):
    bot.send_message(
        call.message.chat.id,
        "🏠 *Bosh menyu*\n\nQuyidagi bo'limlardan birini tanlang:",
        parse_mode="Markdown",
        reply_markup=main_keyboard()
    )
    bot.answer_callback_query(call.id)


# =============================================
#  NOMA'LUM XABAR
# =============================================
@bot.message_handler(func=lambda msg: True)
def unknown(message):
    bot.send_message(
        message.chat.id,
        "Quyidagi tugmalardan birini tanlang 👇",
        reply_markup=main_keyboard()
    )


# =============================================
#  BOTNI ISHGA TUSHIRISH
# =============================================
if __name__ == "__main__":
    print("✅ Otabek Invest boti ishga tushdi...")
    print("⛔ To'xtatish uchun: Ctrl+C")
    bot.infinity_polling()

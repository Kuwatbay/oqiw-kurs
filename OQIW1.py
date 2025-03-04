import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

# Telegram Bot Token
TOKEN = "7758006099:AAHqeu__HDzwhmrc0BzQ1ETpzeyMRRPedFQ"
GROUP_ID = "-1001612125904"  # Группаның ID (минуспен жазылады)
ADMIN_ID = "1494507660"  # Админнің ID (егер топқа емес, жеке жібергіңіз келсе)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# 📌 Бас меню (Кнопкалар)
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Курс туралы ақпарат")],
        [KeyboardButton(text="💰 Бағасы қандай?")],
        [KeyboardButton(text="📞 Байланысу", request_contact=True)]  # Телефон нөмірін сұрайтын батырма
    ],
    resize_keyboard=True
)

# /start командасы
@dp.message(Command("start"))
async def start_command(message: types.Message):
    user = message.from_user.full_name
    await message.answer("Сәлеметсіз бе! Бұл – FAQ бот. Қажетті сұрақты таңдаңыз:", reply_markup=main_keyboard)

    group_message = f"📢 Жаңа қолданушы ботты бастады!\n👤 {user} (@{message.from_user.username})"
    await bot.send_message(GROUP_ID, group_message)

# 📚 Курс туралы ақпарат
@dp.message(lambda message: message.text == "📚 Курс туралы ақпарат")
async def course_info(message: types.Message):
    await message.answer("Біздің курс бағдарламалау негіздерін үйретеді. Толық ақпарат алу үшін бізге жазыңыз!")

# 💰 Бағасы қандай?
@dp.message(lambda message: message.text == "💰 Бағасы қандай?")
async def course_price(message: types.Message):
    await message.answer("Курс бағасы 10 000 теңге. Толық ақпарат алу үшін админге жазыңыз!")

# 📞 Байланысу (Телефон нөмірін қабылдау)
@dp.message(lambda message: message.contact)
async def contact_info(message: types.Message):
    phone_number = message.contact.phone_number
    user_name = message.from_user.full_name

    await message.answer("Рахмет! Сіздің нөміріңіз админге жіберілді. Жақында сізге хабарласады.")

    # Админге немесе топқа хабарлама жіберу
    admin_message = f"📞 Жаңа байланыс сұранысы!\n👤 Аты-жөні: {user_name}\n📱 Нөмірі: {phone_number}"
    await bot.send_message(GROUP_ID, admin_message)  # Группадағы админдерге жібереді
    # await bot.send_message(ADMIN_ID, admin_message)  # Егер жеке админге жібергіңіз келсе, осы жолды ашыңыз

# Белгісіз сұрақтарға жауап
@dp.message()
async def unknown_message(message: types.Message):
    await message.answer("Кешіріңіз, бұл сұраққа жауап бере алмаймын. Басты мәзірден таңдаңыз.")

# Ботты іске қосу
async def main():
    print("FAQ бот іске қосылды...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

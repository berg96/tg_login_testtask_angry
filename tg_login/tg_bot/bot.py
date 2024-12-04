import asyncio
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
import django
import os

from asgiref.sync import sync_to_async
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tg_login.settings')
django.setup()

from django.conf import settings
from users.models import User

load_dotenv()

# TOKEN = settings.TELEGRAM_BOT_TOKEN
TOKEN = os.getenv('TG_BOT_TOKEN')

@sync_to_async
def get_or_create_user(token, telegram_id):
    user, created = User.objects.get_or_create(
        username=token, defaults={"telegram_id": telegram_id}
    )
    if not created:
        user.telegram_id = telegram_id
        user.save()
    return user

async def start_handler(message: Message):
    token = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
    if token:
        user = await get_or_create_user(token, message.from_user.id)  # Асинхронный вызов
        await message.answer(f"Вы успешно авторизовались как {message.from_user.full_name}!")
    else:
        await message.answer("Ошибка: отсутствует токен.")

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.message.register(start_handler, Command("start"))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())

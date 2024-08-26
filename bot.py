import asyncio
from aiogram import Bot, Dispatcher
import logging
from handlers import main_menu, feedback, product_categories
#from config import BOT_TOKEN
import os


BOT_TOKEN = os.getenv('BOT_TOKEN')


if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN found in environment variables.")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_routers(main_menu.router, feedback.router, product_categories.router)


async def main():
    logging.info("Бот запускается...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

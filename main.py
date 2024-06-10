import asyncio
from aiogram import Bot, Dispatcher

from config import TOKEN
from app.handlers import router
from keep_alive import keep_alive

keep_alive()

bot = Bot(token=TOKEN)
dp = Dispatcher()



async def main():
  dp.include_router(router)
  await dp.start_polling(bot)


if __name__ == '__main__':
  asyncio.run(main())
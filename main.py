import asyncio


from decouple import config
from aiogram import  Bot, Dispatcher
import logging
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from hands import router_handler
from text import TEXT_DESC, TEXT_SHORT_DESC
from database.models import async_main


TOKEN = config('TOKEN')
logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


async def main():
    await async_main()
    dp.include_router(router_handler)

    # await bot.set_my_name('Биржа Рекламы')
    # await bot.set_my_description(TEXT_DESC)
    # await bot.set_my_short_description(TEXT_SHORT_DESC)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')
from app.bot.topic import create_topic
from app.core.settings import bot_token
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio
from app.core.settings import logger
from app.bot.handler import dp


async def main():
    logger.info("Запуск Telegram бота")
    bot = Bot(bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await create_topic()
    await dp.start_polling(bot)


if "__main__" == __name__:
    asyncio.run(main())

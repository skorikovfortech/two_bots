from aiogram.filters import CommandStart
from aiogram.types import Message
from app.bot.producer import send_to_kafka
from app.core.settings import logger
from aiogram import Dispatcher
from app.bot.queries import add_user, get_user, save_messages

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    """
    Функция, которая активируется при команде '/start'.
    Проверяет: есть ли этот пользователь в бд или нет,
    если нет, то записывает в бд.
    """
    chat_username = message.chat.username
    chat_id = message.chat.id
    user_tg_id = message.from_user.id
    user = await get_user(user_tg_id)
    if not user:
        await add_user(chat_username, user_tg_id)
        logger.info(f"Новый пользователь: {chat_username} (tg_id={user_tg_id})")

    await message.answer(
        f"Привет! Напиши мне сообщение что бы я его сохранил и отправил в Slack"
    )


@dp.message()
async def handle_message(message: Message):
    user_tg_id = message.from_user.id
    chat_username = message.chat.username
    text = message.text
    user = await get_user(user_tg_id)
    if not user:
        await message.answer(
            f"Для сохранения сообщений, сначала нужно написать команду /start"
        )
        logger.warning(
            f"Сообщение от незарегистрированного пользователя: tg_id={chat_username}"
        )
        return
    await save_messages(user.id, text)
    logger.info(f"Сообщение от {user.username} (tg_id={user_tg_id}): {text}")
    await send_to_kafka({"user_id": user.id, "username": user.username, "text": text})
    await message.answer(f"Ваше сообщение успешно сохранилось")

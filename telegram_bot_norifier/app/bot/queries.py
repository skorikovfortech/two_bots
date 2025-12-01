from sqlalchemy import select, update, insert, delete
from app.core.session import async_session
from app.models import Messages, User


async def get_user(user_tg_id: int):
    async with async_session() as session:
        stmt = select(User).where(User.telegram_id == user_tg_id)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()


async def add_user(username: str, user_tg_id: int):
    async with async_session() as session:
        user = User(username=username, telegram_id=user_tg_id)
        session.add(user)
        await session.commit()
        return user


async def save_messages(user_id, text: str):
    async with async_session() as session:
        message = Messages(text=text, user_id=user_id)
        session.add(message)
        await session.commit()
        return message

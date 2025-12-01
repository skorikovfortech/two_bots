from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from .settings import async_url, sync_url
from sqlalchemy import create_engine


sync_engine = create_engine(sync_url, echo=False)
async_engine = create_async_engine(async_url, echo=False)

async_session = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_async_session():
    async with async_session() as session:
        yield session
        await session.commit()

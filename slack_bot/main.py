import asyncio
from app.consumer import consume_kafka

if __name__ == "__main__":
    asyncio.run(consume_kafka())

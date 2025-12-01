import asyncio
from aiokafka import AIOKafkaProducer
import json

KAFKA_BOOTSTRAP = "kafka:9092"
TOPIC_NAME = "telegram_messages"

producer = None


async def get_producer():
    global producer
    if not producer:
        producer = AIOKafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP)
        await producer.start()
    return producer


async def send_to_kafka(message: dict):
    producer = await get_producer()
    await producer.send_and_wait(TOPIC_NAME, json.dumps(message).encode("utf-8"))

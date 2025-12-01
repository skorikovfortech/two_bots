import asyncio
from aiokafka import AIOKafkaProducer
import json
from app.core.settings import kafka_bootstrap, topic_name


producer = None


async def get_producer():
    global producer
    if not producer:
        producer = AIOKafkaProducer(bootstrap_servers=kafka_bootstrap)
        await producer.start()
    return producer


async def send_to_kafka(message: dict):
    producer = await get_producer()
    await producer.send_and_wait(topic_name, json.dumps(message).encode("utf-8"))

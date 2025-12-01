import asyncio
import json
from aiokafka import AIOKafkaConsumer
from .settings import SLACK_CHANNEL
from .handler import send_to_slack

KAFKA_BOOTSTRAP = "kafka:9092"
TOPIC = "telegram_messages"

async def consume_kafka():
    consumer = AIOKafkaConsumer(
        TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP,
        group_id="slack_consumer_group",
        auto_offset_reset="earliest",
    )

    started = False
    while not started:
        try:
            await consumer.start()
            started = True
            print("Kafka consumer started")
        except Exception as e:
            print("Kafka не готова, пробуем снова через 10 секунд...", e)
            await asyncio.sleep(10)

    try:
        async for msg in consumer:
            data = json.loads(msg.value.decode("utf-8"))
            username = data["username"]
            text = data["text"]
            await send_to_slack(username, text)

    finally:
        await consumer.stop()

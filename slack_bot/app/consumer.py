import asyncio
import json
from aiokafka import AIOKafkaConsumer
from .settings import SLACK_CHANNEL, kafkabootstrap, topic
from .handler import send_to_slack



async def consume_kafka():
    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers=kafkabootstrap,
        group_id="slack_consumer_group",
        auto_offset_reset="earliest",
    )

    try:
        while True:
            try:
                await consumer.start()
                print("Kafka consumer started")
                break
            except Exception as e:
                print("Kafka не готова, пробуем снова через 10 секунд...", e)
                await asyncio.sleep(10)

        async for msg in consumer:
            data = json.loads(msg.value.decode("utf-8"))
            username = data.get("username")
            text = data.get("text")
            await send_to_slack(username, text)

    finally:
        await consumer.stop()
        print("Kafka consumer stopped")
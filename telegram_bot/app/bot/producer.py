import asyncio
from aiokafka import AIOKafkaProducer
import json
from app.core.settings import kafka_bootstrap, topic_name
from aiokafka.admin import NewTopic, AIOKafkaAdminClient


class KafkaProducer:
    def __init__(self, bootstrap_servers=kafka_bootstrap, topic=topic_name):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self._producer = None

    async def start(self):
        if not self._producer:
            self._producer = AIOKafkaProducer(bootstrap_servers=self.bootstrap_servers)
            await self._producer.start()

    async def ensure_topic(self):
        admin = AIOKafkaAdminClient(bootstrap_servers=self.bootstrap_servers)
        await admin.start()
        try:
            existing_topics = await admin.list_topics()
            if self.topic not in existing_topics:
                await admin.create_topics(
                    [NewTopic(name=self.topic, num_partitions=1, replication_factor=1)]
                )
                print(f"Топик '{self.topic}' создан")
        finally:
            await admin.close()

    async def send(self, message: dict):
        await self.start()
        await self._producer.send_and_wait(
            self.topic, json.dumps(message).encode("utf-8")
        )

    async def close(self):
        if self._producer:
            await self._producer.stop()
            self._producer = None


producer = KafkaProducer()

# producer = None


# async def get_producer():
#     global producer
#     if not producer:
#         producer = AIOKafkaProducer(bootstrap_servers=kafka_bootstrap)
#         await producer.start()
#     return producer


# async def send_to_kafka(message: dict):
#     producer = await get_producer()
#     await producer.send_and_wait(topic_name, json.dumps(message).encode("utf-8"))

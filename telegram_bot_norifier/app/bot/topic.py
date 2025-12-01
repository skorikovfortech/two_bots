from aiokafka.admin import AIOKafkaAdminClient, NewTopic
import asyncio

KAFKA_BOOTSTRAP = "kafka:9092"
TOPIC_NAME = "telegram_messages"


async def create_topic():
    admin = AIOKafkaAdminClient(bootstrap_servers=KAFKA_BOOTSTRAP)
    await admin.start()
    try:
        existing_topics = await admin.list_topics()
        if TOPIC_NAME not in existing_topics:
            await admin.create_topics(
                [NewTopic(name=TOPIC_NAME, num_partitions=1, replication_factor=1)]
            )
            print(f"Топик '{TOPIC_NAME}' создан")
        else:
            print(f"Топик '{TOPIC_NAME}' уже существует")
    finally:
        await admin.close()


if __name__ == "__main__":
    asyncio.run(create_topic())

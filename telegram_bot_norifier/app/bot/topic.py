from aiokafka.admin import AIOKafkaAdminClient, NewTopic
import asyncio
from app.core.settings import kafka_bootstrap, topic_name


async def create_topic():
    admin = AIOKafkaAdminClient(bootstrap_servers=kafka_bootstrap)
    await admin.start()
    try:
        existing_topics = await admin.list_topics()
        if topic_name not in existing_topics:
            await admin.create_topics(
                [NewTopic(name=topic_name, num_partitions=1, replication_factor=1)]
            )
            print(f"Топик '{topic_name}' создан")
        else:
            print(f"Топик '{topic_name}' уже существует")
    finally:
        await admin.close()


if __name__ == "__main__":
    asyncio.run(create_topic())

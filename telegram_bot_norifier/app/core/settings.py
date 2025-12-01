from dotenv import load_dotenv
import logging
import os

load_dotenv()

db_protocol = os.getenv("DB_PROTOCOL")
postgres_user = os.getenv("POSTGRES_USER")
postgres_password = os.getenv("POSTGRES_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
kafka_bootstrap = os.getenv("KAFKA_BOOTSTRAP")
topic_name = os.getenv("TOPIC_NAME")

async_url = (
    f"{db_protocol}://{postgres_user}:{postgres_password}@{db_host}:{db_port}/{db_name}"
)


sync_url = (
    f"postgresql://{postgres_user}:{postgres_password}@{db_host}:{db_port}/{db_name}"
)

bot_token = os.getenv("TG_TOKEN")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger("tg_bot")

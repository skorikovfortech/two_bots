import os
from dotenv import load_dotenv


load_dotenv()

SLACK_BOT_TOKEN = os.getenv("BOT_TOKEN")
SLACK_CHANNEL = os.getenv("CHANNEL")

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from app.settings import SLACK_BOT_TOKEN, SLACK_CHANNEL

client = WebClient(token=SLACK_BOT_TOKEN)

async def send_to_slack(username: str, text: str):
    message_text = (
        f"*Новое сообщение из Telegram*\n"
        f"Пользователь: `{username}`\n"
        f"Сообщение: {text}"
    )
    try:
        client.chat_postMessage(channel=SLACK_CHANNEL, text=message_text)
        print("Отправлено в Slack:", message_text)
    except SlackApiError as e:
        print("Ошибка Slack API:", e.response["error"])

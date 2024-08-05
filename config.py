from enum import Enum

from dotenv import dotenv_values
from telethon import TelegramClient

env_config = dotenv_values(".env")

bot_id = env_config["BOT_ID"]
bot_hash = env_config["BOT_HASH"]
bot_token = env_config["BOT_TOKEN"]

bot = TelegramClient("bot", bot_id, bot_hash).start(bot_token=bot_token)


class Messages(Enum):
    ASK_KEYS = ""
    ASK_LOGIN = (
        "Ваш ID не зарегестрирован!",
        " Пожалуйста, введите комманду /login, чтобы продолжить.",
    )

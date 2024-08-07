from dotenv import dotenv_values
from telethon import TelegramClient

env_config = dotenv_values(".env.bot")

bot_id = env_config["BOT_ID"]
bot_hash = env_config["BOT_HASH"]
bot_token = env_config["BOT_TOKEN"]

bot = TelegramClient("./sessions/bot", bot_id, bot_hash).start(
    bot_token=bot_token,
)


class Message:
    KEYS = ["Введите ваш API_ID.", "Введите ваш API_HASH."]
    LOGIN = str(
        "Ваш ID не зарегестрирован!"
        + " Пожалуйста, введите комманду /login, чтобы продолжить."
    )

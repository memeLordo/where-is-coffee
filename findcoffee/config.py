from dotenv import dotenv_values
from telethon import TelegramClient

env_config = dotenv_values(".env.script")

bot_id = int(env_config["BOT_ID"] or 0)
bot_hash = str(env_config["BOT_HASH"] or None)
bot_token = str(env_config["BOT_TOKEN"] or None)

bot = TelegramClient("./sessions/bot", bot_id, bot_hash).start(
    bot_token=bot_token,
)


class Message:
    KEYS = ["Введите ваш API_ID.", "Введите ваш API_HASH."]
    LOGIN = str(
        "Ваш ID не зарегестрирован!"
        + " Пожалуйста, введите комманду /login, чтобы продолжить."
    )

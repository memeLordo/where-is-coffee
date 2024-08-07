from loguru import logger

from .config import bot, bot_token
from .database.orm import ORM


@logger.catch
def start_bot():
    """Start the bot."""
    logger.info("Bot started.")
    try:
        bot.run_until_disconnected()
    except handled_errors as e:
        logger.error(f"Caught {repr(e)}")
        bot.start(bot_token=bot_token)
        bot.send_message(
            "Ошибка сервера, попробуйте повторить попытку позже.",
        )
        bot.run_until_disconnected()


if __name__ == "__main__":
    ORM.create_tables()
    start_bot()

from loguru import logger

from .config import bot
from .database.orm import ORM


def start_bot():
    """Start the bot."""
    logger.info("Bot started.")
    bot.run_until_disconnected()


if __name__ == "__main__":
    ORM.create_tables()
    start_bot()

from loguru import logger

from config import bot
from database import start_db

logger.add(
    "bot_session.log",
    format="{time:DD-MM-YYYY at HH:mm:ss} | {level} | {message}",
    level="INFO",
    rotation="2 MB",
    retention="14 days",
    compression="zip",
)


def main():
    """Start the bot."""
    start_db()
    logger.info("Bot started.")
    bot.run_until_disconnected()


if __name__ == "__main__":
    main()

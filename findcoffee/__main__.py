from loguru import logger

from .config import bot
from .database.orm import ORM

logger.add(
    "sessions/bot_session.log",
    format="{time:DD-MM-YYYY at HH:mm:ss} | {level} | {message}",
    level="INFO",
    rotation="2 MB",
    retention="14 days",
    compression="zip",
)


@logger.catch
def main():
    """Start the bot."""
    ORM.create_tables()
    logger.info("Bot started.")
    bot.run_until_disconnected()


if __name__ == "__main__":
    main()

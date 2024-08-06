from loguru import logger

from .config import bot
from .database.orm import ORM


@logger.catch
def main():
    """Start the bot."""
    ORM.create_tables()
    logger.info("Bot started.")
    bot.run_until_disconnected()


if __name__ == "__main__":
    main()

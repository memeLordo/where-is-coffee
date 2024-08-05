from config import bot
from database import start_db


def main():
    """Start the bot."""
    start_db()
    bot.run_until_disconnected()


if __name__ == "__main__":
    main()

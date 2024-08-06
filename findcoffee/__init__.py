from loguru import logger

from findcoffee import commands, config, database

__all__ = ["commands", "config", "database"]

logger.add(
    "sessions/bot_session.log",
    format="{time:DD-MM-YYYY at HH:mm:ss} | {level} | {message}",
    level="INFO",
    rotation="2 MB",
    retention="14 days",
    compression="zip",
)

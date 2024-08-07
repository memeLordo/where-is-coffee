from asyncio.exceptions import TimeoutError

from loguru import logger

from .config import bot


def error_handler(errors=(Exception,), err_message=" "):

    def wrapper(func):

        async def wrapped(*args, **kwargs):

            try:
                return await func(*args, **kwargs)
            except errors as e:
                logger.error(f"{func.__name__}: {repr(e)} occured.")
                event = args[0]
                await bot.send_message(
                    event.sender,
                    message=err_message,
                )
                logger.info("Reply message sent.")

        return wrapped

    return wrapper


timeout_handler = error_handler((TimeoutError,), err_message="Ошибка.")

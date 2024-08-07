from asyncio.exceptions import TimeoutError

from loguru import logger

import findcoffee.commands as command

from .config import bot


def error_handler(errors=(Exception,), err_message=" "):

    def wrapper(func):

        async def wrapped(*args, **kwargs):
            try:
                event = args[0]
                return await func(*args, **kwargs)

            except TimeoutError:
                logger.info(f"{func.__name__}: aborted.")
                await bot.send_message(event.sender, message=err_message)
                return await command.exit(event)

            except errors as e:
                logger.error(f"{func.__name__}: {repr(e)} occured.")
                await bot.send_message(event.sender, message=err_message)
                logger.info("Reply message sent.")
                return await func(*args, **kwargs)

        return wrapped

    return wrapper


timeout_handler = error_handler((TimeoutError,), err_message="Ошибка.")
value_error_handler = error_handler(ValueError, "Неверное значение.")

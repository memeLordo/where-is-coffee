from asyncio.exceptions import CancelledError

from loguru import logger

from .config import bot


def timeout_handler():

    def wrapper(func):

        async def wrapped(*args, **kwargs):

            try:
                return await func(*args, **kwargs)
            except TimeoutError as e:
                logger.warning(f"{func.__name__}: {repr(e)} occured.")
                # print("Got error! ", repr(e))
                try:
                    event = args[0]
                    await bot.send_message(
                        event.sender,
                        message="Ошибка запроса, повторите попытку.",
                    )
                except CancelledError:
                    try:
                        return await func(*args, **kwargs)
                    except (TimeoutError, CancelledError):
                        pass
                    except Exception as e:
                        logger.exception(f"{repr(e)} still Unresolved")

        return wrapped

    return wrapper


handled_errors = (
    TimeoutError,
    CancelledError,
    Exception,
)

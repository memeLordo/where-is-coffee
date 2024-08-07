from asyncio.exceptions import CancelledError

from loguru import logger

from .config import bot


def timeout_handler():

    def wrapper(func):

        async def wrapped(*args, **kwargs):

            async def send_message(event=args[0], message=" "):
                async with bot:
                    await bot.send_message(
                        event.sender,
                        message,
                    )

            try:
                return await func(*args, **kwargs)
            except TimeoutError as e:
                logger.error(f"Caught {repr(e)}")
                # print("Got error! ", repr(e))
                try:

                    await send_message(
                        message="Ошибка запроса, повторите попытку.",
                    )
                except CancelledError:
                    try:
                        return await func(*args, **kwargs)
                    except Exception as e:
                        logger.exception(f"{repr(e)} still Unresolved")
                        await send_message(
                            message="Ошибка сервера, попробуйте попытку позже",
                        )
        return wrapped

    return wrapper

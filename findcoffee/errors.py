
def timeout_handler():

    def wrapper(func):

        async def wrapped(*args, **kwargs):

            try:
                return await func(*args, **kwargs)
            except TimeoutError as e:
                logger.error(f"Caught {repr(e)}")
                # print("Got error! ", repr(e))

        return wrapped

    return wrapper

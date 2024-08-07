
def timeout_handler():

    def wrapper(func):

        async def wrapped(*args, **kwargs):

            try:
                return await func(*args, **kwargs)

        return wrapped

    return wrapper

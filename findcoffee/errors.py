
def timeout_handler():

    def wrapper(func):

        async def wrapped(*args, **kwargs):

            try:
                return func(*args, **kwargs)
            except errors as e:
                print("Got error! ", repr(e))
                return default_value

        return wrapped

    return wrapper

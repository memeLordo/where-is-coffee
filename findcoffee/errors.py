def error_handler(errors=(Exception,), default_value=""):

    def decorator(func):

        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except errors as e:
                print("Got error! ", repr(e))
                return default_value

        return wrapper

    return decorator

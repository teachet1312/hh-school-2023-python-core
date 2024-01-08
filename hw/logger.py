import datetime
from datetime import datetime


def logger(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        print(f"{func.__name__}: started at {start_time}")
        output = func(*args, **kwargs)
        end_time = datetime.now()
        print(f"{func.__name__}: ended at {end_time}")
        print(f"total time: {end_time - start_time}")
        return output

    return wrapper


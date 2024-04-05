from functools import wraps
from datetime import datetime
import logging

logging.basicConfig(
    filename="functions.log",
    level=logging.DEBUG
)

def log_timestamp(orig_function):

    @wraps(orig_function)
    def replacement(*args, **kwargs):
        logging.debug("Function %s called at %s", orig_function.__name__, datetime.now().ctime())
        result = orig_function(*args, **kwargs)
        return result
    
    return replacement

@log_timestamp
def spam():
    print("calling spam()")

@log_timestamp
def ham():
    print("calling ham()")


def eggs():
    print("calling eggs()")

spam()
spam()
spam()
spam()
eggs()
spam()
ham()
ham()
ham()

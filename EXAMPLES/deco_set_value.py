from deco_timestamp import log_timestamp
# decorator

def set_return_value(return_value):
    # function wrapper (wraps original function)
    def wrapper(old_func):

        # replacement function (original function name now refers to this function)
        def replacement(*args, **kwargs):
            # log here
            return return_value
        return replacement
    
    return wrapper


@log_timestamp
@set_return_value(42)
def spam():
    return 1, 2, 3

#  spam = set_return_value(42)(spam)

@set_return_value(10)
def ham():
    return "absinthe"

spam_result = spam()
print(f"{spam_result = }")

ham_result = ham()
print(f"{ham_result = }")

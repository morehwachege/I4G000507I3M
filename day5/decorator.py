
def name_decorator(said_function):
    def wrapper():
        said_function()
        said_function()
    return wrapper


@name_decorator
def print_name():
    return "James"

print(print_name())



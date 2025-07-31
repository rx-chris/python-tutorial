# function with no arguments
def hello_world():
    print("Hello world!")


# function call
hello_world()


def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2


total = sum(7, 2)
print(total)


def multiple_items(*args):
    print(args)
    print(type(args))


# *args will be treated as a tuple
multiple_items("Dave", "John", "Sara")


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


# **kwargs will be treated as a dictionary
mult_named_items(first="Dave", last="Gray")

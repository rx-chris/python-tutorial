# Variable declared in the global scope
name = "Dave"


def greeting():
    # Variable declared in the local scope
    color = "blue"
    print("Hello, " + name + ". Your favorite color is " + color + ".")


greeting()  # Hello, Dave. Your favorite color is blue.

print(name)  # Dave

# This will raise an error
# print(color)

# try:
#     print(x)
# except:
#     print("An error occurred")

# try:
#     print(x)
# except NameError:
#     print("A NameError occurred. This means that something was not defined.")

# y = 2
# try:
#     print(y / 0)
# except ZeroDivisionError:
#     print("A ZeroDivisionError occurred. Please do not divide by zero.")

# y = 2
# try:
#     print(y / 2)
# except ZeroDivisionError:
#     print("A ZeroDivisionError occurred. Please do not divide by zero.")
# else:
#     print("This will run if no exceptions were raised.")

# y = 2
# try:
#     print(y / 2)
# except ZeroDivisionError:
#     print("A ZeroDivisionError occurred. Please do not divide by zero.")
# else:
#     print("This will run if no exceptions were raised.")
# finally:
#     print("This will run no matter what.")

# y = 2

# try:
#     if not type(y) is str:
#         raise TypeError("Only strings are allowed.")
# except ZeroDivisionError:
#     print("A ZeroDivisionError occurred. Please do not divide by zero.")
# except Exception as e:
#     print(f"An error occurred: {e}")
# else:
#     print("This will run if no exceptions were raised.")
# finally:
#     print("This will run no matter what.")


# y = 2

# try:
#     if not type(y) is str:
#         raise TypeError("Only strings are allowed.")
# except ZeroDivisionError:
#     print("A ZeroDivisionError occurred. Please do not divide by zero.")
# except Exception as e:
#     print(f"An error occurred: {e}")
# else:
#     print("This will run if no exceptions were raised.")
# finally:
#     print("This will run no matter what.")


# try:
#     raise Exception("This is a custom error message.")
# except Exception as e:
#     print(f"An error occurred: {e}")


class JustNotCoolError(Exception):
    pass


try:
    raise JustNotCoolError("This just isn't cool man.")
except JustNotCoolError as e:
    print(f"A JustNotCoolError occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

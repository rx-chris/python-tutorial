count = 1


def increment_count():
    global count
    count += 1  # This will raise an error if 'global' is not used


print("before increment: ", count)
increment_count()
print("after increment: ", count)

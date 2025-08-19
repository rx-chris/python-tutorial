# recursive function to add one to a number until it reaches 9 or greater
def add_one(num):

    # base case: if num is 9 or greater, return num + 1
    if (num >= 9):
        return num + 1

    # recursive case: increment num by 1 and call add_one() again
    total = num + 1
    print(total)

    return add_one(total)


# calling the function with an initial value of 0
add_one(0)

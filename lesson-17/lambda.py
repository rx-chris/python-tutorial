def squared(x): return x ** 2


print(squared(5))


def add(x, y): return x + y

###############################

# high-order function that returns a lambda function


def funcBuilder(x):
    return lambda num: num + x


add_ten = funcBuilder(10)
add_twenty = funcBuilder(20)

print(add_ten(7))     # 17
print(add_twenty(7))  # 27

########################


numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

###############################

odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))

#############################


numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

print(sum(numbers, 10))


names = ['Dave Gray', 'Sara Ito', 'John Jacob Jingleheimerschmidt']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)

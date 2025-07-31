users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []

print("Dave" in users)  # True
print("Dave" in data)  # True
print("Dave" in emptylist)  # False

print("")
# index and index ranges
print(users[0])  # Dave
print(users[-2])  # John

print(users.index('Sara'))  # 2

print(users[0:2])  # ['Dave', 'John']
print(users[1:])  # ['John', 'Sara']
print(users[-3:-1])  # ['Dave', 'John']

print("")
# length of list
print(len(data))  # 3

print("")
# append to end of list
users.append('Elsa')
print(users)  # ['Dave', 'John', 'Sara', 'Elsa']

print("")
# extend list with another list
users += ['Jason']
print(users)  # ['Dave', 'John', 'Sara', 'Elsa', 'Jason']

users.extend(['Robert', 'Jimmy'])
print(users)  # ['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']

# users.extend(data)
# print(users)

print("")
# insert list item at index 0
users.insert(0, 'Bob')
# ['Bob', 'Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']
print(users)

# insert multiple list items at index 2
users[2:2] = ['Eddie', 'Alex']
# ['Bob', 'Dave', 'Eddie', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']
print(users)

print("")
# replace items in list
users[1] = 'James'
# ['Bob', 'James', 'Eddie', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']
print(users)
users[1:3] = ['Robert', 'JPJ']
# ['Bob', 'Robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']
print(users)

print("")
# remove item in list
users.remove('Bob')
# ['Robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']
print(users)

# remove last item in list
print(users.pop())  # Jimmy
# ['Robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert']
print(users)

# remove item in list at index 0
del users[0]
print(users)  # ['JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'Robert']

# clear all items in list
data.clear()
print(data)  # []

print("")
# sort items in list
users[1:2] = ['dave']
print(users)

# sort default (ascending uppercase followed by lowercase)
users.sort()
print(users)  # ['Elsa', 'JPJ', 'Jason', 'John', 'Robert', 'Sara', 'dave']

# sort with callback as key
users.sort(key=str.lower)
print(users)  # ['dave', 'Elsa', 'Jason', 'John', 'JPJ', 'Robert', 'Sara']

nums = [4, 42, 78, 1, 5]

# reverses the order of the list
nums.reverse()
print(nums)  # [5, 1, 78, 42, 4]

# sort list in descending order
# nums.sort(reverse=True)
# print(nums)  # [78, 42, 5, 4, 1]

# return sorted list in descending order
print(sorted(nums, reverse=True))  # [78, 42, 5, 4, 1]

# orginal list remains unchanged
print(nums)  # [5, 1, 78, 42, 4]

print("")

# copy list
# copy method
numscopy = nums.copy()
# copy constructor
mynums = list(nums)
# index range notation
mycopy = nums[:]

print(numscopy)  # [5, 1, 78, 42, 4]
print(mynums)  # [5, 1, 78, 42, 4]
mycopy.sort()
print(mycopy)  # [1, 4, 5, 42, 78]
print(nums)  # [5, 1, 78, 42, 4]

print("")
# list constructor and data type
print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)

# Tuples

print("")
# create tuple
mytuple = tuple(('Dave', 42, True))
anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)  # ('Dave', 42, True)
print(type(mytuple))  # <class 'tuple'>
print(type(anothertuple))  # <class 'tuple'>

print("")
# update items in tuple
newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)  # ('Dave', 42, True, 'Neil')

print("")
# unpack tuple
(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print("")
print(anothertuple.count(2))

# literal assignment
import math
first = "Dave"
last = "Gray"

# type checking
print(type(first))  # <class 'str'>
print(type(first) == str)  # True
print(isinstance(first, str))  # True

# constructor function
pizza = str('Pepperoni')

print(type(pizza))  # <class 'str'>
print(type(pizza) == str)  # True
print(isinstance(pizza, str))  # True

# concatenation
fullname = first + " " + last
print(fullname)

# casting a number to a string
decade = str(1980)
print(type(decade))

print(decade)  # 1980

statement = "I like rock music fro the " + decade + "s."

print(statement)  # I like rock music fro the 1980s.

# multiple lines
multiline = '''
Hey, how are you?

I was just checking in.
                All good?
'''

print(multiline)

# escaping special characters
sentence = 'I\'m back at work!\t Hey!\n\nWhere\'s this at \\located?'

print(sentence)

# string methods
phrase = "This is good"
print(phrase)

# to lower case
print(phrase.lower())
# to uppercase
print(phrase.upper())
# capitalize first letter
print(phrase.title())
# replace text
print(phrase.replace('good', 'ok'))
# length of string
print(len(phrase))
# starts with text
print(phrase.startswith("T"))
# ends with text
print(phrase.endswith("Z"))

print("")

phrase2 = "    pizza is delicious  "
# remove white spaces on both ends
print(phrase2.strip())
# remove white spaces on left side
print(phrase2.lstrip())
# remove white spaces on right side
print(phrase2.rstrip())

print("")


# center and justifying text
title = "MENU"
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))


# string index values
word = 'delicious'

# 2nd character in word
print(word[1])  # e
# last character
print(word[-1])  # s
# 2nd character up to excluding last character
print(word[1:-1])  # eliciou
# 2nd character up end of string
print(word[1:])  # elicious

# Boolean data type
# literal assignment
myvalue = True
othervalue = False
# cast to boolean via constructor
x = bool('something')  # True
y = bool(0)  # False

print(type(x))  # <class 'bool'>
print(isinstance(x, bool))  # True

# integer data type
# literal assignment
price = 100
# cast from float to int via constructor
x = int(3.00)

print(type(price))  # <class 'int'>
print(isinstance(price, int))  # True
print(isinstance(x, int))  # True

# float data type
# literal assignment
gpa = 3.28
# cast from int to float via constructor
y = float(2)

print(type(gpa))  # <class 'float'>
print(isinstance(gpa, float))  # True
print(isinstance(y, float))  # True

# complex number literal
comp_value = 5 + 3j

print(type(comp_value))  # <class 'complex'>
print(comp_value.real)  # 5.0
print(comp_value.imag)  # 3.0

# built-in numeric functions
num = 14.52

print(abs(num * -1))  # 14.5
print(round(num))  # 15
print(round(num, 1))  # 14.5

# math module

print(math.pi)  # 3.141592653589793
print(math.sqrt(num))  # 3.81051177665153
print(math.ceil(num))  # 15
print(math.floor(num))  # 14

# cast a string to a number
zipcode = "10001"
zip_value = int(zipcode)

print(type(zip_value))  # <class 'int'>

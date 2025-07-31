value = 1

# # while loop if break statement
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# # while loop with continue statement and else statement
# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))

names = ["Dave", "Sara", "John"]
# for x in names:
#     print(x)

# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Sara":
#         break
#     print(x)

# for x in names:
#     if x == "Sara":
#         continue
#     print(x)

# # loop through range from 0 to 3
# for x in range(4):
#     print(x)

# # loop through range from 2 to 3 (exclude 4)
# for x in range(2, 4):
#     print(x)

# # loop through range from 5 to 100 with increment of 5
# for x in range(5, 101, 5):
#     print(x)
# else:
#     print("Glad that\'s over!")

names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")

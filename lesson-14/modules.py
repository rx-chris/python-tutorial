# basic import
import sys

# import with alias
import random as rdm

# import specific item
from math import pi
from enum import Enum

# import custom module
import kansas

# list all items in 'random' module
for item in dir(rdm):
    print(item)

print(kansas.capital)

# Python standard Library

# Modules with dir()
# helps you to find out functions and variables available in the module.

import math
print(dir(math))

# Math Module

# pi - 3.14 e = 2.718
# sqrt(),  pow(3,2) = 9, fact(5)=120 , ceil(4.000000001)=5, floor(4.9999999999)=4
# math.sin(), pow(e,x)

# Random Module.
import random

# randint()

random.randint(1,10)

random.random() # Generates a decimal between 0 and 1.

action = ["stone","paper","scissor"]
print(random.choice(action))

# Shuffling of list values.
# 3-2-4-1-5
cards = [1,2,3,4,5]
random.shuffle(cards)
print(cards)

# random.seed(100)
print(random.randint(1,100))

# random.seed(100)
print(random.randint(1,100))

# Platform Module
import platform
print(platform.system())
print(platform.release())
print(platform.machine())
print(platform.processor())
print(platform.python_version())
from types import MethodDescriptorType

from anyio.abc import ObjectStream
from fontTools.ttLib.tables.S__i_l_f import Classes
from zmq.sugar.attrsettr import AttributeSetter

# Imperative Programming:


x = 10
x = x + 5
x = x * 2
x = x / 10

print(x)


# Procedural Programming

# Banking System for a User

balance = 1000

def deposit(amount):
    global balance
    balance = balance + amount

def withdraw(amount):
    global balance
    balance = balance - amount

deposit(500)
withdraw(200)
print(balance)

# Problems
# 1. Global State is Dangerous.
# 2. Functions can modify data unpredictably.


# What is Object Oriented Programming ?
# 1. Create a collection of interacting objects :
#  - Each Object has some data, exposes some type of behaviour and will represent
#    a real world entity.

# Components Of OOPS:
# 1. Objects
# 2. Classes
# 3. Attributes
# 4. Methods
# 5. Interaction Between Objects



class Bank:

    def __inti__(self, balance):
        self.balance = balance

# This is the initial State.
account1 = Bank(1000)

# This is the modification of the data.
# State is changed, but the identity remains same.
account1.balance = 3000



# Counter Class.

class Counter:

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

# Here state -> count
# Behaviour --> increment()

c1 = Counter()
c1.increment()


#  Example 2 : Mobile Phone

class Phone:

    def __init__(self):
        self.battery = 50

    def call(self):
        self.battery -= 5

    def charge(self):
        self.battery +=50


# Object Int





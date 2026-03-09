
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def sum(self,a,b):
        return a+b

# THE FIRST PARAMETER is always "self"

# Object Creation vs Object Initialization
#
# 1. Object Creation -> Is just allocation of the memory for a particular object.
# 2. Object Initialization -> Is giving the parameters the value while creating the object.not
#
# Object Initialization occurs after creation

# Method : __init__
# Constructor -> Special method named __init__ that is automatically created after an object is created.

class Student:

    # USE ONLY FOR INITIALIZATION.
    def __init__(self, name, age):
        self.name = name
        self.age = age




s1 = Student("John", 22)

# Steps :
# 1. Object of Student class is created.
# 2.  Method __init__ is called on that object
# 3. Student.__init__(s1,name,age)
# 4. Attrinbutes are initialized


# Method : __new__
# Constructor -> Special method named __new__ which helps in creating a new instance and returning the object.

class BankAccount:

    def __new__(cls):
        instance = super().__new__(cls)
        return instance

    def __init__(self, balance):
        self.balance = balance

b1 = BankAccount()
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name}"

# class subClass(ParentClass):
#     pass

# Student class is derived from class Person.
class Student(Person):
    pass


## Special Method: __str__() --> Converts the object to a readable string.
# usecases : print(object), str(object)
# MUST RETURN A string.

person1 = Person("Ashraf")
print(person1) # Represents what the object is about.


## issubclass() --> Checks the Relationship between two classes.
# issubclass(Class A, ClassB) --> True if Class A inherits from Class B

print(issubclass(Student, Person))

## isinstance() --> If an object belongs to a particular class or not.

print(isinstance(person1, Student))
print(isinstance(person1, Person))

## is Operator --> 1. Memory Location, Object Identify

p1 = Person("Ashraf")
p2 = Person("Eshan")
p3 = Person("Ashraf")

print(p1 is p2)
print(p1 is p3)



## super() --> Returns a reference to the nearest parent class.
## Employee > Manager > FoodManager
class Employee:
    def __str__(self):
        return "Employee"

class Manager(Employee):
    def __str__(self):
        return "Manager -> Parent Class is: " + super().__str__()

class FoodManager(Manager):
    def __str__(self):
        return "Food Manager -> Parent Class is: " + super().__str__()

m = Manager()
print(m)

fM = FoodManager()
print(fM)


## In general, when we inherit a class, all the class variables, methods, instance variables will be inherited.
## Until we override it.


class Employee:
    noOfEmployees=0 # Class Variable will be shared among all instances.
    def __init__(self,name):
        self.name = name # Instance Variable.
        Employee.noOfEmployees+=1

    def greet(self):
        return f"My name is {self.name}"

class Developer(Employee):
    pass

d = Developer("John")
d1 = Developer("Mike")
print(d.greet())
print(d1.greet())
print(d.noOfEmployees)


# Class Variables are shared among all instances.
# Instance Variable belongs to each object.


class A:
    def say(self):
        return "A"
class B(A):
    def say(self):
        return "B"

b = B()
print(b.say())
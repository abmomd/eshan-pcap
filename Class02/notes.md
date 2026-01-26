
# Object Interaction

Objects can:
- Call each other's methods
- Pass Data
- Collaborate to complete tasks

```python

class Engine:
    
    def start(self):
        print("Engine Started")


class Car:
    def __inti__(self):
        self.engine = Engine()
    
    def start(self):
            self.engine.start()

```

```python

class Course:
    def show_course(self):
        print("This is OOP ")
class Student:
    def __init__(self,):
        self.course = Course()
    def show_course(self):
        self.course.show_course()
s1=Student()
s1.show_course()

```

## Object Equality vs Identity

Equality is comparing the states of two objects
Identity is comparing the memory of two objects

```python

a = [1, 2]
b = [1, 2]

print(a == b) # Compare States --> true
print(a is b) # Compare Identity --> false
```

# Attributes

Variables associated with an object that stores data describing the object's state.

- Attributes are created dynamically
- They belong to an object


```python

class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

s1 = Student("Eshan", 14)
s2 = Student("Ari", 14)

# Data is stored as a dictionary

# {name : "Eshan", age : 14}

```

## Why SELF Exists ?


Self is a reference to the current object that is automatically passed to instance methods.
```python
def __init__(self, name, age):
        self.name = name
        self.age = age
        
# s1 = Student("Eshan",14) --> Student.__init__ (s1,"Eshan",14)


```



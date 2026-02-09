# Notes – Stack, Inherited Stack, Queue, and Balanced Parenthesis

1. Stack and AddingStack (Subclass)

A stack is a linear data structure that follows the LIFO (Last In First Out) principle.

Basic operations:
push(value) → inserts an element at the top  
pop() → removes the top element  
peek() → returns the top element without removing it  
is_empty() → checks if the stack is empty  

Stack Class

```python
class Stack:
    def __init__(self):
        self._stack = []

    def push(self, value):
        self._stack.append(value)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self._stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._stack[-1]

    def is_empty(self):
        return len(self._stack) == 0
```

AddingStack (Subclass of Stack)

AddingStack maintains a running sum of elements present in the stack.

Rules:
- When push(value) is called, value is added to sum
- When pop() is called, removed value is subtracted from sum
- sum always represents the total of elements currently in the stack

```python
class AddingStack(Stack):
    def __init__(self):
        super().__init__()
        self.sum = 0

    def push(self, value):
        super().push(value)
        self.sum += value

    def pop(self):
        value = super().pop()
        if value is not None:
            self.sum -= value
        return value
```

Example Usage

```python
s = AddingStack()
s.push(10)
s.push(20)
s.push(30)

print(s.sum)   # 60
s.pop()
print(s.sum)   # 30
```

2. Queue Class

A queue is a linear data structure that follows the FIFO (First In First Out) principle.

Operations:
put(value) → insert element at the rear  
get() → remove and return the front element  
peek() → view the front element without removing it  
is_empty() → check if queue is empty  
size() → return number of elements  

Queue Implementation Using Class

```python
class Queue:
    def __init__(self):
        self._queue = []

    def put(self, value):
        self._queue.append(value)

    def get(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self._queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self._queue[0]

    def is_empty(self):
        return len(self._queue) == 0

    def size(self):
        return len(self._queue)
```

Example Usage

```python
q = Queue()
q.put(10)
q.put(20)
q.put(30)

print(q.get())   # 10
print(q.peek())  # 20
```

3. Balanced Parenthesis Problem

Problem Statement

Given a string containing parentheses:
(), {}, []

Check whether the parentheses are balanced.

Rules:
- Every opening bracket must have a matching closing bracket
- Brackets must close in the correct order
- Closing bracket cannot appear before its matching opening bracket

Examples:
()[]{} → Balanced  
(] → Not Balanced  
([{}]) → Balanced  
((() → Not Balanced  

Algorithm Using Stack

1. Create an empty stack
2. Traverse the expression character by character
3. If opening bracket → push it onto the stack
4. If closing bracket:
   - stack must not be empty
   - top of stack must match the closing bracket
5. After traversal, stack must be empty for the expression to be balanced

Python Solution

```python
def is_balanced(expression):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}

    for ch in expression:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or stack[-1] != matching[ch]:
                return False
            stack.pop()

    return len(stack) == 0
```

Example Usage

```python
print(is_balanced("()[]{}"))    # True
print(is_balanced("(]"))        # False
print(is_balanced("([{}])"))    # True
print(is_balanced("((()"))      # False
```

Key Takeaways

- Stack follows LIFO and is useful for backtracking problems
- Inheritance allows extending stack functionality (AddingStack)
- Queue follows FIFO and models real-life waiting systems
- Balanced Parenthesis is a classic DSA problem solved using stack

# 📂 Processing Text and Binary Files – Notes

## 🎯 Learning Objectives

By the end of this section, you should be able to:

* Read data from text and binary files.
* Write data into text and binary files.
* Process files line by line.
* Read entire files at once.
* Understand the difference between text and binary file processing.
* Use file streams efficiently.

---

# 🧠 1. Reading Data from Files

Python provides several methods to read data from files.

---

## 📖 read()

The `read()` method reads characters (text files) or bytes (binary files).

### Syntax

```python
file.read(size)
```

* `size` is optional.
* If omitted, the entire file is read.

### Example

```python
file = open("story.txt", "r")

content = file.read()

print(content)

file.close()
```

---

### Read First 10 Characters

```python
file = open("story.txt", "r")

content = file.read(10)

print(content)

file.close()
```

---

## 🌍 Real-Life Example

A news website loads the entire contents of an article before displaying it to users.

---

# 📖 readline()

Reads exactly one line from a text file.

### Example

```python
file = open("students.txt", "r")

line = file.readline()

print(line)

file.close()
```

---

### Reading Multiple Lines

```python
file = open("students.txt", "r")

print(file.readline())
print(file.readline())
print(file.readline())

file.close()
```

---

## 🌍 Real-Life Example

A chatbot processes conversation logs one message at a time.

---

# 📖 readlines()

Reads all lines and stores them inside a list.

### Example

```python
file = open("students.txt", "r")

lines = file.readlines()

print(lines)

file.close()
```

---

### Output

```python
[
    "John\n",
    "Emma\n",
    "Mike\n"
]
```

---

## 🌍 Real-Life Example

A school system loads an entire attendance sheet into memory.

---

# 📖 readinto()

Used with binary files.

Reads bytes directly into a bytearray.

### Example

```python
data = bytearray(1024)

file = open("image.png", "rb")

file.readinto(data)

file.close()
```

---

## 🌍 Real-Life Example

Image editors and video processing software frequently use byte arrays.

---

# ✍️ 2. Writing Data to Files

Python uses the `write()` method.

---

## Writing Text

```python
file = open("report.txt", "w")

file.write("Python is awesome!")

file.close()
```

---

### Output in File

```text
Python is awesome!
```

---

## Writing Multiple Lines

```python
file = open("report.txt", "w")

file.write("Line 1\n")
file.write("Line 2\n")
file.write("Line 3\n")

file.close()
```

---

## 🌍 Real-Life Example

A banking application generates monthly account statements.

---

# 🖼️ Writing Binary Data

### Example

```python
data = bytearray([65, 66, 67, 68])

file = open("binary.bin", "wb")

file.write(data)

file.close()
```

---

## 🌍 Real-Life Example

A camera application saves image data to a file.

---

# 🔄 Iterating Through a File

Files are iterable objects.

This means they can be used directly in a loop.

---

## Example

```python
for line in open("students.txt", "rt"):
    print(line, end="")
```

---

### Output

```text
John
Emma
Mike
```

---

## Advantages

* Memory efficient
* Reads one line at a time
* Suitable for very large files

---

## 🌍 Real-Life Example

Log analysis systems process huge log files line by line.

---

# 📂 Text Files vs Binary Files

| Text Files      | Binary Files       |
| --------------- | ------------------ |
| Human readable  | Not human readable |
| .txt, .csv, .py | .jpg, .png, .mp3   |
| Use strings     | Use bytes          |
| Mode: r, w      | Mode: rb, wb       |

---

# 🧪 Exercise 1

## Question

What does `readlines()` return when used on an empty file?

### Example

```python
file = open("empty.txt", "r")

print(file.readlines())
```

### Answer

```python
[]
```

An empty list.

---

# 🧪 Exercise 2

## Code

```python
for line in open("file", "rt"):
    for char in line:
        if char.lower() not in "aeiouy ":
            print(char, end='')
```

---

## What Does It Do?

The program:

* Reads the file line by line.
* Examines every character.
* Removes vowels:

  * a
  * e
  * i
  * o
  * u
  * y
* Removes spaces.
* Prints only consonants and punctuation.

---

### Example

File Content:

```text
Hello World
```

Output:

```text
HllWrld
```

---

# 🧪 Exercise 3

## Question

Read the entire image into a bytearray called `image`.

### Code

```python
try:
    stream = open("image.png", "rb")

    # Missing line

    stream.close()

except IOError:
    print("failed")

else:
    print("success")
```

---

## Solution

```python
image = bytearray(stream.read())
```

Complete Code:

```python
try:
    stream = open("image.png", "rb")

    image = bytearray(stream.read())

    stream.close()

except IOError:
    print("failed")

else:
    print("success")
```

---

# 🌍 Real-Life Applications

## 📸 Image Viewer

```python
image = bytearray(stream.read())
```

Loads image bytes.

---

## 🎵 Music Player

```python
audio = stream.read()
```

Loads song data.

---

## 🎥 Video Streaming

```python
for chunk in stream:
    process(chunk)
```

Reads video data efficiently.

---

## 📊 Data Analytics

```python
for line in open("sales.csv"):
    analyze(line)
```

Processes sales records.

---

# ⚠️ Common Mistakes

## Forgetting to Close Files

❌

```python
file = open("data.txt")
```

✅

```python
file = open("data.txt")
file.close()
```

---

## Using Text Mode for Images

❌

```python
open("photo.jpg", "r")
```

✅

```python
open("photo.jpg", "rb")
```

---

## Reading Huge Files at Once

❌

```python
data = file.read()
```

May consume excessive memory.

✅

```python
for line in file:
    process(line)
```

---

# 🚀 Best Practices

* Use `with open()` whenever possible.
* Process large files line by line.
* Use binary modes for images, videos, PDFs, and audio files.
* Close files properly.
* Use exception handling for file operations.

---

# 🎯 Summary

### Reading Methods

| Method      | Purpose                    |
| ----------- | -------------------------- |
| read()      | Read characters/bytes      |
| readline()  | Read one line              |
| readlines() | Read all lines into a list |
| readinto()  | Read bytes into bytearray  |

---

### Writing Methods

| Method  | Purpose             |
| ------- | ------------------- |
| write() | Write text or bytes |

---

### File Iteration

```python
for line in open("file.txt"):
    print(line)
```

Simple and memory efficient.

---

### Key Idea

Files are one of the most important ways programs interact with the real world.

Whether you're building:

* Banking software
* AI systems
* Games
* Websites
* Data analytics tools

file processing is a fundamental skill every Python programmer must master.

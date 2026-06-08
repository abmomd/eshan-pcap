# 📂 File Handling in Python – Complete Notes

File handling allows Python programs to:

- Read data from files
- Write data into files
- Store information permanently
- Process text and binary data

Without files, all program data disappears when the program terminates.

---

# 🧠 1️⃣ What is a File?

A file is a collection of data stored on a storage device such as:

- Hard Disk
- SSD
- USB Drive
- Cloud Storage

Examples:

```text
notes.txt
students.csv
image.png
report.pdf
```

---

# 🧠 2️⃣ What is a Stream?

When Python works with a file, it doesn't access the file directly.

Instead, it uses a **stream**.

A stream is an abstract connection between:

```text
Program ↔ File
```

Think of it like a pipe through which data flows.

---

## Real-Life Analogy

Imagine drinking juice:

```text
Juice Box → Straw → You
```

The straw is the stream.

Similarly:

```text
File → Stream → Program
```

---

# 🧠 3️⃣ Opening a File

Before a file can be used, it must be opened.

---

## Syntax

```python
stream = open(file_name, mode)
```

Example:

```python
stream = open("notes.txt", "r")
```

---

# 🧠 4️⃣ Why Open a File?

Opening a file:

- Creates a stream object
- Connects the program to the file
- Defines how the file will be used

---

# 🧠 5️⃣ Closing a File

After processing:

```python
stream.close()
```

must be called.

---

## Why?

Closing:

- Saves changes
- Releases resources
- Prevents corruption

---

## Example

```python
file = open("notes.txt", "r")

print(file.read())

file.close()
```

---

# 🧠 6️⃣ File Open Modes

The mode determines what operations are allowed.

---

# 🔹 Read Mode (`r`)

Used when reading existing files.

```python
open("data.txt", "r")
```

Allowed:

✅ Read

Not Allowed:

❌ Write

---

## Example

```python
file = open("students.txt", "r")
```

---

# 🔹 Write Mode (`w`)

Used when creating or overwriting files.

```python
open("article.txt", "w")
```

Allowed:

✅ Write

Not Allowed:

❌ Read

---

## Example

```python
file = open("article.txt", "w")

file.write("Python is awesome!")

file.close()
```

---

# ⚠️ Important

If the file exists:

```python
"w"
```

erases previous contents.

---

# 🔹 Update Mode (`r+`, `w+`)

Allows both:

✅ Read

✅ Write

---

## Example

```python
file = open("data.txt", "r+")
```

---

# 🧠 Exercise 1

## Question

How do you create a new text file and write an article into it?

---

## ✅ Answer

```python
open("article.txt", "w")
```

---

# 🧠 7️⃣ Text Files vs Binary Files

Python supports two major file types.

---

# 🔹 Text Files

Contain human-readable text.

Examples:

```text
.txt
.csv
.py
.md
```

Processed using:

```python
TextIOBase
```

---

## Example

```python
file = open("notes.txt", "r")
```

---

# 🔹 Binary Files

Contain raw bytes.

Examples:

```text
.jpg
.png
.mp3
.mp4
.exe
```

Processed using:

```python
BufferedIOBase
```

---

## Example

```python
file = open("image.jpg", "rb")
```

---

# 🧠 Common Binary Modes

| Mode | Meaning |
|--------|--------|
| rb | Read binary |
| wb | Write binary |
| ab | Append binary |

---

# 🧠 8️⃣ Text Encoding

Text files store characters using encodings.

Common encodings:

- UTF-8
- ASCII
- UTF-16

---

## Syntax

```python
open(file, mode, encoding="utf-8")
```

---

## Example

```python
file = open(
    "story.txt",
    "r",
    encoding="utf-8"
)
```

---

# 🧠 9️⃣ Complete open() Syntax

```python
open(
    file_name,
    mode=open_mode,
    encoding=text_encoding
)
```

---

## Example

```python
file = open(
    "report.txt",
    mode="w",
    encoding="utf-8"
)
```

---

# 🧠 🔟 Predefined Streams

Python automatically opens three streams when the program starts.

---

# 🔹 sys.stdin

Standard Input

Usually:

```python
input()
```

uses this stream.

---

## Example

```python
import sys

data = sys.stdin.readline()
```

---

# 🔹 sys.stdout

Standard Output

Used by:

```python
print()
```

---

## Example

```python
import sys

sys.stdout.write("Hello")
```

---

# 🔹 sys.stderr

Standard Error Output

Used for error messages.

---

## Example

```python
import sys

sys.stderr.write("Error occurred")
```

---

# 🧠 Real-Life Analogy

Think of a restaurant:

```text
Customer Order → stdin
Chef Output → stdout
Complaint Desk → stderr
```

---

# 🧠 1️⃣1️⃣ IOError Exception

File operations may fail.

When they do:

```python
IOError
```

is raised.

---

## Common Reasons

- File missing
- Permission denied
- Disk full
- Invalid path

---

# ✅ Example

```python
try:
    file = open("abc.txt")

except IOError:
    print("Cannot open file")
```

---

# 🧠 1️⃣2️⃣ errno Property

Every IOError contains:

```python
error.errno
```

which stores the error code.

---

## Example

```python
import errno

try:
    file = open("abc.txt")

except IOError as error:
    print(error.errno)
```

---

# 🧠 Common errno Values

| Constant | Meaning |
|-----------|----------|
| errno.ENOENT | File not found |
| errno.EACCES | Permission denied |
| errno.EEXIST | File already exists |

---

# 🧠 Exercise 2

## Question

What does:

```python
errno.EACCES
```

mean?

---

## ✅ Answer

```text
Permission Denied
```

---

## Real-Life Example

Trying to edit:

```text
C:\Windows\system32
```

without administrator rights.

---

# 🧠 Exercise 3

## Code

```python
import errno

try:
    stream = open("file", "rb")

    print("exists")

    stream.close()

except IOError as error:

    if error.errno == errno.ENOENT:
        print("absent")
    else:
        print("unknown")
```

---

## Assuming File Does NOT Exist

### Output

```python
absent
```

---

## Why?

Opening:

```python
open("file", "rb")
```

fails.

Python raises:

```python
IOError
```

with:

```python
errno.ENOENT
```

meaning:

```text
No such file or directory
```

---

# 🌍 Real-Life Examples

---

# 🏫 Student Report Generator

```python
file = open("students.txt", "r")
```

Read student records.

---

# 📰 News Article Writer

```python
file = open("article.txt", "w")
```

Create and save articles.

---

# 📸 Photo Viewer

```python
file = open("photo.jpg", "rb")
```

Read image bytes.

---

# 🎵 Music Player

```python
file = open("song.mp3", "rb")
```

Read audio data.

---

# ☁️ Cloud Storage System

```python
try:
    upload_file()

except IOError:
    print("Upload failed")
```

---

# ⚠️ Common Mistakes

| Mistake | Fix |
|----------|------|
| Forgetting close() | Always close files |
| Using wrong mode | Choose correct mode |
| Reading non-existent file | Use try-except |
| Using text mode for images | Use binary mode |

---

# 🚀 Best Practices

✅ Use `try-except` when opening files

✅ Close files after use

✅ Use UTF-8 encoding

✅ Check `errno` for detailed diagnosis

✅ Use appropriate file mode

---

# 🎯 Summary

- Files must be opened before use
- Files should be closed after use
- Streams connect programs to files
- Common modes:
  - `r` → read
  - `w` → write
  - `r+` → update
- Text and binary files are processed differently
- `IOError` handles file operation failures
- `errno` helps diagnose file errors
- Python provides:
  - `stdin`
  - `stdout`
  - `stderr`

---

# 🧠 Final Thought

File handling allows programs to remember information even after they stop running.

Almost every real-world application uses files:

- Banking systems
- Websites
- Games
- Databases
- AI applications

Mastering file handling is a crucial step toward becoming a strong Python developer.
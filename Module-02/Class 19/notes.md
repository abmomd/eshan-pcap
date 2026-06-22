# 🖥️ Python OS Module – Complete Notes

## 🎯 Learning Objectives

By the end of this module, you should be able to:

* Obtain information about the operating system.
* Create and remove directories.
* Navigate through directories.
* List files and folders.
* Execute operating system commands.
* Understand the difference between Windows and Unix environments.

---

# 🧠 1. What is the OS Module?

The `os` module allows Python programs to interact directly with the operating system.

Think of it as a bridge between:

```text
Python Program ↔ Operating System
```

Using `os`, Python can:

* Create folders
* Delete folders
* Navigate directories
* Execute terminal commands
* Obtain system information

---

# 🌍 Real-Life Example

Imagine you're building:

* A file explorer
* A backup system
* A deployment script
* A cloud storage application

All these applications need the OS module.

---

# 🧠 2. Getting Operating System Information

Python provides:

```python
import os

os.uname()
```

This returns information about the current operating system.

---

## Example

```python
import os

info = os.uname()

print(info)
```

---

## Common Attributes

| Attribute | Meaning               |
| --------- | --------------------- |
| system    | Operating System Name |
| nodename  | Machine Name          |
| release   | OS Release            |
| version   | OS Version            |
| machine   | Hardware Architecture |

---

## Example Output (Linux)

```text
posix.uname_result(
    system='Linux',
    nodename='ubuntu',
    release='6.5.0',
    version='Ubuntu',
    machine='x86_64'
)
```

---

# 🌍 Real-Life Example

A software installer may need to detect:

```python
if os.uname().system == "Linux":
    install_linux_version()
```

---

# 🧠 3. os.name

A simpler way to identify the operating system.

---

## Example

```python
import os

print(os.name)
```

---

## Possible Outputs

| Output | Meaning          |
| ------ | ---------------- |
| posix  | Unix/Linux/macOS |
| nt     | Windows          |
| java   | Jython           |

---

## Example

Linux:

```text
posix
```

Windows:

```text
nt
```

---

# 🧪 Exercise 1

## Code

```python
import os

print(os.name)
```

### Running on Unix

Output:

```text
posix
```

---

# 🌍 Real-Life Example

A deployment script may behave differently:

```python
if os.name == "nt":
    print("Windows commands")

else:
    print("Unix commands")
```

---

# 🧠 4. Creating Directories

Use:

```python
os.mkdir()
```

---

## Syntax

```python
os.mkdir(path)
```

---

## Relative Path Example

```python
import os

os.mkdir("Projects")
```

Creates:

```text
Current Folder
└── Projects
```

---

## Absolute Path Example

```python
os.mkdir("/home/user/Projects")
```

---

# ⚠️ Important

If folder already exists:

```python
FileExistsError
```

is raised.

---

## Example

```python
try:
    os.mkdir("Projects")

except FileExistsError:
    print("Folder already exists.")
```

---

# 🌍 Real-Life Example

A project generator:

```python
Project/
├── src/
├── tests/
└── docs/
```

automatically creates folders.

---

# 🧠 5. Creating Nested Directories

Use:

```python
os.makedirs()
```

---

## Example

```python
import os

os.makedirs("Python/Projects/WebApp")
```

Creates:

```text
Python
└── Projects
    └── WebApp
```

---

## Difference

### mkdir()

Creates:

```text
hello
```

only.

---

### makedirs()

Creates:

```text
a/b/c/d
```

all at once.

---

# 🌍 Real-Life Example

Cloud storage systems create nested folders automatically.

---

# 🧠 6. Listing Directory Contents

Use:

```python
os.listdir()
```

---

## Example

```python
import os

print(os.listdir())
```

Output:

```python
[
    'file1.txt',
    'Projects',
    'image.png'
]
```

---

## Specify Path

```python
print(os.listdir("Projects"))
```

---

# Important

The following are NOT shown:

```text
.
..
```

---

# 🧪 Exercise 2

## Code

```python
import os

os.mkdir("hello")

print(os.listdir())
```

---

### Output

Current directory contents including:

```python
[
    'hello'
]
```

plus any existing files/folders.

---

# 🌍 Real-Life Example

A file manager application displays:

```python
os.listdir()
```

results.

---

# 🧠 7. Current Working Directory

Use:

```python
os.getcwd()
```

---

## Example

```python
import os

print(os.getcwd())
```

Output:

```text
/home/user/projects
```

---

# 🌍 Real-Life Example

A deployment tool needs to know where it's running.

---

# 🧠 8. Changing Directories

Use:

```python
os.chdir()
```

---

## Example

```python
import os

os.chdir("Projects")
```

---

## Verify

```python
print(os.getcwd())
```

---

# 🌍 Real-Life Example

A build script moves into project folders before compiling.

---

# 🧠 9. Removing Directories

Use:

```python
os.rmdir()
```

---

## Example

```python
import os

os.rmdir("Projects")
```

---

## Condition

Folder must be empty.

---

# ⚠️ Otherwise

```python
OSError
```

is raised.

---

# 🧠 10. Removing Nested Directories

Use:

```python
os.removedirs()
```

---

## Example

```python
os.removedirs(
    "Python/Projects/WebApp"
)
```

Removes:

```text
WebApp
Projects
Python
```

if empty.

---

# 🌍 Real-Life Example

Cleanup scripts delete generated folder structures.

---

# 🧠 11. Running System Commands

Use:

```python
os.system()
```

---

## Example

```python
import os

os.system("mkdir hello")
```

---

### Windows

Executes:

```cmd
mkdir hello
```

---

### Linux

Executes:

```bash
mkdir hello
```

---

# Return Value

```python
result = os.system("mkdir hello")
```

Success:

```python
0
```

Failure:

```python
non-zero
```

---

# 🌍 Real-Life Example

Deployment automation:

```python
os.system("git pull")
os.system("python app.py")
```

---

# 🏢 Real-World Use Cases

---

## 1. Backup System

```python
os.mkdir("Backup")
```

Create backup folders.

---

## 2. File Explorer

```python
os.listdir()
```

Display files.

---

## 3. Installer Software

```python
os.makedirs("App/Data/Logs")
```

Create application folders.

---

## 4. Build Automation

```python
os.chdir("project")
```

Move into project folder.

---

## 5. Deployment Scripts

```python
os.system("git pull")
```

Run deployment commands.

---

# ⚠️ Common Mistakes

---

## Creating Existing Directory

❌

```python
os.mkdir("hello")
```

twice.

Raises:

```python
FileExistsError
```

---

## Removing Non-Empty Directory

❌

```python
os.rmdir("project")
```

when files exist.

Raises:

```python
OSError
```

---

## Wrong Directory Change

❌

```python
os.chdir("missing_folder")
```

Raises:

```python
FileNotFoundError
```

---

# 🚀 Best Practices

✅ Use exception handling

```python
try:
    os.mkdir("data")

except FileExistsError:
    pass
```

---

✅ Use `os.path.exists()` before creation

---

✅ Prefer `makedirs()` for nested structures

---

✅ Check return values from `os.system()`

---

# 🎯 Summary

| Function        | Purpose                   |
| --------------- | ------------------------- |
| os.uname()      | System information        |
| os.name         | Operating system type     |
| os.mkdir()      | Create directory          |
| os.makedirs()   | Create nested directories |
| os.listdir()    | List files/folders        |
| os.getcwd()     | Current directory         |
| os.chdir()      | Change directory          |
| os.rmdir()      | Remove directory          |
| os.removedirs() | Remove nested directories |
| os.system()     | Execute OS commands       |

---

# 🧠 Final Thought

The `os` module allows Python programs to interact with the operating system itself.

Almost every professional application uses it:

* Installers
* Deployment tools
* Backup systems
* Cloud platforms
* Build automation tools
* File management software

Mastering the OS module is an important step toward becoming a real-world Python developer.

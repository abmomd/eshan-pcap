# 🛰️ Problem 5: Mission Control Directory Navigator

## 📘 Story

NASA stores mission data in nested folders.

Example:

```text
Missions/
├── Mars/
│   ├── Rover/
│   └── Images/
```

Engineers frequently need to move between directories and inspect contents.

Your job is to build a navigation utility.

---

## 🎯 Your Task

Create:

```text
Missions/
├── Mars/
│   ├── Rover/
│   └── Images/
```

Then:

1. Display current directory.
2. Move into Missions.
3. Display contents.
4. Move into Mars.
5. Display contents.
6. Return back to original directory.

---

## ⚙️ Requirements

Use:

- `mkdir()` / `makedirs()`
- `getcwd()`
- `chdir()`
- `listdir()`

---

## 🧪 Sample Output

```text
Current Directory:
/Users/Ashraf

Moved to:
Missions

Contents:
Mars

Moved to:
Mars

Contents:
Rover
Images

Returned to original directory.
```
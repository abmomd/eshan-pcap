# 🚀 1. NASA Deep Space Communication System

## 📘 Story

NASA has launched a rover to Mars.

Every few seconds, the rover sends telemetry data back to Earth.

A communication file contains thousands of lines like:

```text
TEMP:25
TEMP:27
TEMP:29
TEMP:ERROR
TEMP:31
```

Mission Control wants software that can process these readings.

---

## 🎯 Your Task

Build a program that:

- Reads telemetry data from a file
- Extracts temperature values
- Ignores corrupted readings
- Calculates:
  - Highest temperature
  - Lowest temperature
  - Average temperature

---

## ⚙️ Exception Handling

Handle:

- FileNotFoundError
- ValueError
- IOError

---

## 💡 Challenge

Use `sys.stdin` so that engineers can pipe files directly:

```
python mars.py < telemetry.txt
```
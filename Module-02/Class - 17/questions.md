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

# 🏦 2. International Bank Fraud Detection System

## 📘 Story

A bank receives transaction logs continuously.

Each transaction looks like:

```text
TXN1001,5000
TXN1002,15000
TXN1003,ERROR
TXN1004,9000
```

Some transactions are corrupted due to network issues.

The fraud department wants a monitoring system.

---

## 🎯 Your Task

Read transaction records and:

- Count valid transactions
- Ignore invalid transactions
- Calculate total transaction amount
- Identify transactions above ₹10,000

---

## ⚙️ Exception Handling

Handle:

- ValueError
- IndexError
- IOError

---

## 💡 Challenge

Accept data using:

```python
sys.stdin
```

instead of `input()`.

# 🎮 3. Online Gaming Leaderboard Processor

## 📘 Story

A multiplayer game stores scores inside a text file.

Example:

```text
Alice,1200
Bob,900
Charlie,1500
David,ERROR
Emma,2000
```

The gaming company wants to generate a leaderboard automatically.

---

## 🎯 Your Task

Read the file and:

- Ignore invalid score entries
- Find:
  - Highest score
  - Lowest score
  - Average score
- Display Top 3 Players

---

## ⚙️ Exception Handling

Handle:

- FileNotFoundError
- ValueError
- IndexError

---

## 💡 Bonus

Allow the file name to be entered by the user.

# 🚗 4. Smart Highway Speed Monitoring System

## 📘 Story

A smart highway uses cameras to record vehicle speeds.

The file contains:

```text
KA01AB1234,80
KA02CD5678,110
KA03EF9012,ERROR
KA04GH3456,140
```

Speed above 120 km/h is considered overspeeding.

---

## 🎯 Your Task

Create a program that:

- Reads all vehicle records
- Detects overspeeding vehicles
- Ignores corrupted records
- Counts:
  - Total vehicles
  - Overspeeding vehicles
  - Average speed

---

## ⚙️ Exception Handling

Handle:

- ValueError
- IOError
- AssertionError

---

## 💡 Challenge

Generate a new file called:

```text
violators.txt
```

containing all overspeeding vehicles.

# 🎵 5. Music Streaming Analytics System

## 📘 Story

A music company records song streams.

Data file:

```text
ShapeOfYou,5000
Believer,3000
Perfect,ERROR
Thunder,4500
```

Management wants daily analytics.

---

## 🎯 Your Task

Read the file and determine:

- Total streams
- Most played song
- Average streams per song

Ignore corrupted entries.

---

## ⚙️ Exception Handling

Handle:

- ValueError
- FileNotFoundError
- IOError

---

## 💡 Challenge

Save the final report into:

```text
report.txt
```


# 🤖 6. AI Chat Server Log Analyzer

## 📘 Story

An AI chatbot receives millions of messages every day.

A log file contains:

```text
SUCCESS
SUCCESS
FAILED
SUCCESS
FAILED
FAILED
SUCCESS
```

The operations team wants daily statistics.

---

## 🎯 Your Task

Read the log file and calculate:

- Total requests
- Successful requests
- Failed requests
- Success percentage

---

## ⚙️ Exception Handling

Handle:

- FileNotFoundError
- IOError

---

## 💡 Challenge

Accept logs through:

```python
sys.stdin
```

so the program can process live streams.


# 🛰️ 7. Space Station Oxygen Monitoring System

## 📘 Story

An orbiting space station records oxygen levels every hour.

Data file:

```text
95
94
93
ERROR
91
89
```

The life-support team wants alerts whenever oxygen drops below 90%.

---

## 🎯 Your Task

Read oxygen readings and:

- Ignore corrupted readings
- Find minimum oxygen level
- Generate alert if any reading < 90

---

## ⚙️ Exception Handling

Handle:

- ValueError
- FileNotFoundError
- AssertionError

---

## 💡 Challenge

Create:

```text
alerts.txt
```

containing all dangerous readings.
# 🌍 Advanced OS Module + File I/O Projects

These projects are designed to combine:

* OS Module
* File Handling
* Directory Management
* Exception Handling
* Data Processing
* Report Generation

The goal is to simulate real-world software systems rather than isolated coding exercises.

---

# 🚀 Project 1: NASA Mission Data Logger

## 📘 Story

NASA launches missions to different planets.

Every mission generates:

* Images
* Sensor Reports
* Temperature Logs

Scientists want software that automatically organizes mission data and generates reports.

---

## 🎯 Your Task

Ask the user for:

```text
Mission Name
Planet Name
```

Example:

```text
Artemis
Mars
```

---

## 📁 Directory Structure

Create:

```text
Artemis/
├── Images/
├── Reports/
├── Logs/
└── mission_info.txt
```

---

## 📄 mission_info.txt

Store:

```text
Mission: Artemis
Planet: Mars
Status: Active
```

---

## 📄 temperature_log.txt

Create:

```text
Logs/temperature_log.txt
```

Store sample temperatures:

```text
23
25
24
28
22
```

---

## 📊 Data Analysis

Read the temperature file and calculate:

* Highest Temperature
* Lowest Temperature
* Average Temperature

---

## 📄 summary.txt

Generate:

```text
Reports/summary.txt
```

containing:

```text
Mission Summary
---------------
Highest Temperature : XX
Lowest Temperature  : XX
Average Temperature : XX
```

---

## ⚙️ Concepts Used

* os.makedirs()
* os.listdir()
* File Writing
* File Reading
* Exception Handling

---

# 🏦 Project 2: Smart Bank Branch Management System

## 📘 Story

A national bank is opening branches across India.

Each branch stores:

* Customer Data
* Transactions
* Reports

Managers want branch setup to be fully automated.

---

## 🎯 Your Task

Ask the user for:

```text
Branch Name
```

Example:

```text
BangaloreBranch
```

---

## 📁 Directory Structure

Create:

```text
BangaloreBranch/
├── Customers/
├── Transactions/
├── Reports/
└── branch_info.txt
```

---

## 📄 customers.txt

Create:

```text
Customers/customers.txt
```

Store:

```text
Rahul
Amit
Sneha
Priya
```

---

## 📄 transactions.txt

Create:

```text
Transactions/transactions.txt
```

Store:

```text
5000
7000
1000
9000
```

---

## 📊 Analysis

Calculate:

* Total Transaction Amount
* Highest Transaction
* Average Transaction

---

## 📄 monthly_report.txt

Generate:

```text
Reports/monthly_report.txt
```

containing the analysis.

---

## 💡 Bonus

Use:

```python
os.system()
```

to display the report.

---

# 🎮 Project 3: Game Studio Save Manager

## 📘 Story

A game studio wants to manage save files for players.

Each player receives a dedicated folder.

---

## 📁 Directory Structure

Create:

```text
GameData/
├── Player1/
│   ├── save.txt
│   └── stats.txt
├── Player2/
│   ├── save.txt
│   └── stats.txt
```

---

## 📄 save.txt

Example:

```text
Level: 12
Coins: 450
Lives: 3
```

---

## 📄 stats.txt

Example:

```text
Enemies Defeated: 210
Hours Played: 18
```

---

## 🎯 Your Task

Read every player's data.

Generate:

```text
leaderboard.txt
```

sorted by:

```text
Coins
```

Highest first.

---

## 📊 Example Output

```text
Player1 -> 450 Coins
Player2 -> 320 Coins
```

---

## ⚙️ Concepts Used

* Directory Traversal
* File Reading
* Sorting
* Report Generation

---

# ☁️ Project 4: Cloud Storage Usage Analyzer

## 📘 Story

A cloud company wants to monitor storage consumption for customers.

---

## 📁 Directory Structure

Create:

```text
CloudStorage/
├── User1/
│   └── usage.txt
├── User2/
│   └── usage.txt
├── User3/
│   └── usage.txt
```

---

## 📄 usage.txt

Example:

```text
150
230
180
```

(MB used per day)

---

## 🎯 Your Task

Read every usage file.

Calculate:

* Total Usage per User
* Overall Usage
* Highest Usage User

---

## 📄 storage_report.txt

Generate:

```text
User1 : 560 MB
User2 : 740 MB
User3 : 420 MB

Highest Usage User : User2
```

---

## ⚙️ Concepts Used

* os.listdir()
* File Reading
* Aggregation
* Report Generation

---

# 🤖 Project 5: AI Training Experiment Tracker

## 📘 Story

An AI company trains machine learning models daily.

Each experiment produces:

* Accuracy
* Loss
* Epochs

Management wants an automated experiment tracker.

---

## 📁 Directory Structure

Create:

```text
AIExperiments/
├── Experiment1/
│   └── results.txt
├── Experiment2/
│   └── results.txt
├── Experiment3/
│   └── results.txt
```

---

## 📄 results.txt

Example:

```text
Accuracy: 91
Loss: 0.23
Epochs: 15
```

---

## 🎯 Your Task

Read all experiments.

Determine:

* Best Accuracy
* Best Experiment

---

## 📄 best_model.txt

Generate:

```text
Best Experiment : Experiment2
Accuracy : 95%
```

---

## 💡 Bonus

Delete experiments whose accuracy is below:

```text
80%
```

using:

```python
os.removedirs()
```

---

## ⚙️ Concepts Used

* File Reading
* Directory Traversal
* Data Analysis
* Directory Removal

---

# 🛰️ Project 6: Space Station Oxygen Monitoring System

## 📘 Story

A space station records oxygen levels every hour.

The data is stored day-wise.

Scientists need automatic monitoring and alerts.

---

## 📁 Directory Structure

Create:

```text
SpaceStation/
├── Day1/
│   └── oxygen.txt
├── Day2/
│   └── oxygen.txt
├── Day3/
│   └── oxygen.txt
```

---

## 📄 oxygen.txt

Example:

```text
96
94
92
88
95
```

---

## 🎯 Your Task

Read all oxygen readings.

Generate alerts whenever oxygen falls below:

```text
90
```

---

## 📄 alerts.txt

Example:

```text
Day1 -> 88
Day3 -> 85
```

---

## 📄 final_report.txt

Generate:

```text
Minimum Oxygen : XX
Maximum Oxygen : XX
Average Oxygen : XX
Number of Alerts : XX
```

---

## ⚙️ Concepts Used

* File Reading
* File Writing
* Data Processing
* Alert Generation
* Directory Traversal

---

# 🎯 Skills Practiced

Across these projects you will use:

✅ os.name

✅ os.getcwd()

✅ os.chdir()

✅ os.listdir()

✅ os.mkdir()

✅ os.makedirs()

✅ os.rmdir()

✅ os.removedirs()

✅ os.system()

✅ File Reading

✅ File Writing

✅ Exception Handling

✅ Data Analysis

✅ Report Generation

These projects closely resemble tasks performed by:

* DevOps Engineers
* Cloud Engineers
* Backend Developers
* Data Engineers
* AI Platform Engineers
* System Administrators
* Automation Engineers

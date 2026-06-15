# 🌍 Real-Life File Handling & Exception Handling Projects – Solutions

This file contains solutions for all 7 real-world projects.

---

# 🚀 1. NASA Deep Space Communication System

## Solution

```python
try:
    filename = input("Enter telemetry file name: ")

    with open(filename, "r") as file:
        temperatures = []

        for line in file:
            try:
                temp = int(line.strip().split(":")[1])
                temperatures.append(temp)
            except ValueError:
                continue

        print("Highest Temperature:", max(temperatures))
        print("Lowest Temperature:", min(temperatures))
        print("Average Temperature:", sum(temperatures) / len(temperatures))

except FileNotFoundError:
    print("Telemetry file not found.")

except IOError:
    print("Unable to read file.")
```

---

# 🏦 2. International Bank Fraud Detection System

## Solution

```python
try:
    filename = input("Enter transaction file name: ")

    valid_count = 0
    total_amount = 0

    with open(filename, "r") as file:

        for line in file:
            try:
                txn_id, amount = line.strip().split(",")
                amount = float(amount)

                valid_count += 1
                total_amount += amount

                if amount > 10000:
                    print("High Value Transaction:", txn_id)

            except ValueError:
                print("Corrupted transaction skipped.")

    print("Valid Transactions:", valid_count)
    print("Total Amount:", total_amount)

except FileNotFoundError:
    print("Transaction file not found.")

except IOError:
    print("Unable to read transaction file.")
```

---

# 🎮 3. Online Gaming Leaderboard Processor

## Solution

```python
try:
    filename = input("Enter leaderboard file: ")

    players = []

    with open(filename, "r") as file:

        for line in file:
            try:
                name, score = line.strip().split(",")
                players.append((name, int(score)))

            except ValueError:
                continue

    players.sort(key=lambda x: x[1], reverse=True)

    print("Highest Score:", players[0])
    print("Lowest Score:", players[-1])

    avg = sum(score for _, score in players) / len(players)
    print("Average Score:", avg)

    print("\nTop 3 Players")

    for player in players[:3]:
        print(player)

except FileNotFoundError:
    print("Leaderboard file not found.")

except IOError:
    print("Unable to process leaderboard.")
```

---

# 🚗 4. Smart Highway Speed Monitoring System

## Solution

```python
try:
    total = 0
    count = 0
    violators = []

    with open("vehicles.txt", "r") as file:

        for line in file:
            try:
                vehicle, speed = line.strip().split(",")
                speed = int(speed)

                count += 1
                total += speed

                if speed > 120:
                    violators.append(vehicle)

            except ValueError:
                continue

    average_speed = total / count

    print("Total Vehicles:", count)
    print("Average Speed:", average_speed)
    print("Violators:", len(violators))

    with open("violators.txt", "w") as output:
        for vehicle in violators:
            output.write(vehicle + "\n")

except IOError:
    print("File processing failed.")
```

---

# 🎵 5. Music Streaming Analytics System

## Solution

```python
try:
    songs = {}

    with open("streams.txt", "r") as file:

        for line in file:
            try:
                song, streams = line.strip().split(",")
                songs[song] = int(streams)

            except ValueError:
                continue

    total_streams = sum(songs.values())

    top_song = max(songs, key=songs.get)

    average = total_streams / len(songs)

    print("Total Streams:", total_streams)
    print("Most Played Song:", top_song)
    print("Average Streams:", average)

    with open("report.txt", "w") as report:
        report.write(f"Total Streams: {total_streams}\n")
        report.write(f"Top Song: {top_song}\n")
        report.write(f"Average Streams: {average}\n")

except FileNotFoundError:
    print("Streams file missing.")

except IOError:
    print("Unable to generate report.")
```

---

# 🤖 6. AI Chat Server Log Analyzer

## Solution

```python
try:
    success = 0
    failed = 0

    with open("logs.txt", "r") as file:

        for line in file:

            status = line.strip()

            if status == "SUCCESS":
                success += 1

            elif status == "FAILED":
                failed += 1

    total = success + failed

    percentage = (success / total) * 100

    print("Total Requests:", total)
    print("Successful:", success)
    print("Failed:", failed)
    print("Success Rate:", percentage)

except FileNotFoundError:
    print("Log file not found.")

except IOError:
    print("Unable to read logs.")
```

---

# 🛰️ 7. Space Station Oxygen Monitoring System

## Solution

```python
try:
    readings = []
    alerts = []

    with open("oxygen.txt", "r") as file:

        for line in file:
            try:
                value = int(line.strip())

                readings.append(value)

                if value < 90:
                    alerts.append(value)

            except ValueError:
                continue

    print("Minimum Oxygen Level:", min(readings))

    if alerts:
        print("ALERT! Dangerous oxygen levels detected.")

    with open("alerts.txt", "w") as output:

        for value in alerts:
            output.write(str(value) + "\n")

except FileNotFoundError:
    print("Oxygen data file missing.")

except IOError:
    print("Unable to process oxygen data.")
```

---

# 🎯 Concepts Covered

These projects collectively use:

✅ open()

✅ close() via with statement

✅ Read Mode (`r`)

✅ Write Mode (`w`)

✅ Exception Handling

✅ FileNotFoundError

✅ IOError

✅ ValueError

✅ String Parsing

✅ Lists & Dictionaries

✅ Report Generation

✅ Real-World Data Processing

---

# 🚀 Industry Connections

These projects resemble real systems used in:

* NASA Mission Control
* Banking Fraud Detection
* Gaming Analytics
* Smart Transportation
* Music Streaming Platforms
* AI Monitoring Systems
* Space Station Life Support Systems

The same concepts form the foundation of professional data-processing software.

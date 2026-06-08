try:
    with open("nasa.txt", "r") as file:
        temperatures = []

        for line in file:
            try:
                temp = int(line.strip().split(":")[1])
                temperatures.append(temp)
            except ValueError:
                continue

        print("Highest Temeperatur:", max(temperatures))
        print("Lowest Temeperatur:", min(temperatures))
        print("Average Temeperatur:", sum(temperatures) / len(temperatures))



except FileNotFoundError:
    print("Telemetry File not found.")
except IOError:
    print("Unable to read the file.")
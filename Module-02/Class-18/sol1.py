try:
    filename = input("Enter file name: ")

    counts = {}

    with open(filename, "r") as file:

        for line in file:

            for char in line.lower():

                if 'a' <= char <= 'z':

                    if char in counts:
                        counts[char] += 1
                    else:
                        counts[char] = 1

    for letter in sorted(counts.keys()):
        print(letter, "->", counts[letter])

except FileNotFoundError:
    print("File not found.")

except IOError:
    print("Unable to read file.")
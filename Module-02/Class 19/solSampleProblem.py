import os

# Save the original directory
original_directory = os.getcwd()

try:
    # Create the directory structure
    os.makedirs("Missions/Mars/Rover")
    os.makedirs("Missions/Mars/Images")

    # Step 1: Display current directory
    print("Current Directory:")
    print(original_directory)

    # Step 2: Move into Missions
    os.chdir("Missions")

    print("\nMoved to:")
    print(os.path.basename(os.getcwd()))

    # Step 3: Display contents
    print("\nContents:")
    for item in os.listdir():
        print(item)

    # Step 4: Move into Mars
    os.chdir("Mars")

    print("\nMoved to:")
    print(os.path.basename(os.getcwd()))

    # Step 5: Display contents
    print("\nContents:")
    for item in os.listdir():
        print(item)

    # Step 6: Return to original directory
    os.chdir(original_directory)

    print("\nReturned to original directory.")
    print("Current Directory:")
    print(os.getcwd())

except FileExistsError:
    print("Directory structure already exists.")

except FileNotFoundError:
    print("Directory not found.")

except Exception as e:
    print("An error occurred:", e)
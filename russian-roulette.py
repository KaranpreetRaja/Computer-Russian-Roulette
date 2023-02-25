import os
import random

root_dir = input("Please enter the root directory (e.g. C:\\): ")
if not os.path.exists(root_dir):
    print("The specified directory does not exist.")
    exit()

print("Welcome to the game.")
print("There is a 1 in 6 chance that the script will delete EVERYTHING")
input("You have been warned. Press Enter to continue...")

if random.randint(1, 6) == 1:
    print("BOOM!")
    for root, dirs, files in os.walk(root_dir, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
            except:
                print(f"Failed to delete the file, {file_path}")
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                os.rmdir(dir_path)
            except:
                print(f"Failed to delete the directory, {dir_path}")
else:
    print("Click! You got lucky, this time...")

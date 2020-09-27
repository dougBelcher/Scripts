# Examples
import os
from pathlib import Path


# os.chdir('\\Users\\WRA1523\\AppData\\Local\\Programs\\Python\\Python37-32')

# Post-3.5
# print(f"\nPost-3.5: ")
# with os.scandir() as entries:
#    for entry in entries:
#        print(f"{entry.name}")

# List all files in a directory using scandir()
# print(f"\nList all files in a directory using scandir: ")
# basepath = '\\Users\\WRA1523\\AppData\\Local\\Programs\\Python\\Python37-32'
# with os.scandir(basepath) as entries:
#    for entry in entries:
#        if entry.is_file():
#            print(entry.name)

# Create a single directory
# try:
#    os.mkdir('example_dir/')
# except FileExistsError as exc:
#    print(exc)

# os.makedirs('xkcd', exist_ok=True)

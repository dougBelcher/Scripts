# Misc operating system interfaces
import os
from pathlib import Path

# print(f"{os.name}")

print(f"{os.getcwd()}")

# os.chdir('\\Users\\WRA1523\\AppData\\Local\\Programs\\Python\\Python37-32')

# with open('data.txt', 'r') as f:
#     data = f.read()

# Pre-3.5
# print(f"\nPre-3.5: ")
# entries = os.listdir()
# for entry in entries:
#    print(f"{entry}")

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

# List all subdirectories using scandir()
# print(f"\nList all subdir using scandir: ")
# basepath = '\\Users\\WRA1523\\AppData\\Local\\Programs\\Python\\Python37-32'
# with os.scandir(basepath) as entries:
#    for entry in entries:
#        if entry.is_dir():
#            print(entry.name)

# Create a single directory
# try:
#    os.mkdir('example_dir/')
# except FileExistsError as exc:
#    print(exc)

# Create a single dir with Path
# p = Path('example_dir')
# p.mkdir(exist_ok=True)

# Make multiple directories
# os.makedirs('2020/02/10')

# Get .txt files
# for f_name in os.listdir(
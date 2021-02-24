# Intro Bite 01. F-strings and a simple if/else
MIN_DRIVING_AGE = '16'

name = input("Input name: ")
age = input("age: ")

# print(f'{name} is allowed to drive if MIN_DRIVING_AGE>age else {name} is not allowed to drive')
# print(f'Doug is allowed to drive {if MIN_DRIVING_AGE>age else Doug is not allowed to drive}')
print(f'{age} {name} is allowed to drive' if age > MIN_DRIVING_AGE else '{name} is not allowed')
drive = "{name} is {drive} to drive".format(drive="allowed" if age > MIN_DRIVING_AGE else "not allowed")

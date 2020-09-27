# Input two numbers and determine if the diff is an int

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
num3 = float(num1) - float(num2)

print(f"The difference between {float(num1)} and {float(num2)} is an integer? {num3.is_integer()}!")
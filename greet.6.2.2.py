# Write a function called greet() that takes one string parameter called name and displays the text "Hello < name >!", where < name > is replaced with the value of the name parameter.


def greet(name):
    print(f"Hello {name}!")


response = input("Enter name: ")
greet(response)

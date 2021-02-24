# Bite 15. Enumerate 2 sequences
names = ['Julian', 'Bob', 'PyBites', 'Dante', 'Martin', 'Rodolfo']
countries = ['Australia', 'Spain', 'Global', 'Argentina', 'USA', 'Mexico']

for index, name in enumerate(names, start=1):
    print(f"{index}. {name}\t")
def collatz(nbr):
    if nbr % 2 == 0:
        print(nbr // 2)
        return nbr // 2
    else:
        print(3 * nbr + 1)
        return 3 * nbr + 1


print('Enter number:')
try:
    number = int(input())
    while number > 1:
        number = collatz(number)
except ValueError:
    print('There was an error.')

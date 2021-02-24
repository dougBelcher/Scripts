#   020. Zfill
#   https://docs.python.org/3/library/stdtypes.html?highlight=zfill#str.zfill

for i in range(1, 6):
    print(f'{str(i).zfill(3)}')

for i in range(1, 6):
    print(f'{str(i).zfill(5)}')

for i in range(-3, 2):
    print(f'{str(i).zfill(3)}')

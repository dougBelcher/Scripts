total = 0
x = 0
while True:
    Num = input('Enter a number: ')
    # if done is enter, end the loop and complete the calcs
    if Num == 'done':
        break
    else:
        try:
            total += float(Num)
        except:
            print('bad input')
            continue
    # count up the nbr of entries
    x += 1
# print out the sum, count, and avg
print(total, x, float(total) / x)

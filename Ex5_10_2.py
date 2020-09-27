total = 0
x = 0
Largest = None
Smallest = None
while True:
  Num = input('Enter a number: ')
# if done is enter, end the loop and complete the calcs
  if Num == 'done':
    break
  else:
    try:
      if Smallest is None or Num < Smallest:
        Smallest = Num
      if Largest is None or Num > Largest:
        Largest = Num
    except:
      print('bad input')
      continue
# print out the sum, count, and avg
print(Largest, Smallest)

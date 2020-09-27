from computepay import computepay
try:
  Hours = input('Enter Hours: ')
  Rate = input('Enter Rate: ')
  Pay = computepay(Hours, Rate)
  print Pay
except:
  print 'Please enter numbers for Hours and Rate'
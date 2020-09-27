from computegrade import computegrade
try:
  Score = input('Enter score between 0.0 and 1.0: ')
  Grade = computegrade(Score)  
  print Grade
except:
  print 'Score must be between 0.0 and 1.0'
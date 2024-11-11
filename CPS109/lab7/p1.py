# A run is a sequence of adjacent repeated values. Write a program that generates a
# sequence of 20 random die tosses and then prints the die values, marking the runs by
# including them in parentheses, like this: 1 2 (5 5) 3 1 2 4 3 (2 2 2 2) 3 6 (5 5) 6 3 1
# Use the following pseudocode:
# Set a boolean variable inRun to false.
# For each valid index i in the list
# if inRun
# If values[i] is different from the preceding value
# Print )
# inRun = false
# if values[i] is the same as the following value and not inRun
# print (
# inRun = true
# Print values[i]
# If inRun, print )

import random
def run(inRun=False):
    for i in range(20):
      if inRun:
        if values[i] != values[i-1]:
          print(')',end=' ')
          inRun=False
      if inRun==False and i!=19:
        if values[i] == values[i+1]:
          print('(',end=' ')
          inRun=True
      print(values[i] , end=' ')
    print()

values=[]
for count in range(20):
  n=random.randrange(1,7)
  values.append(n)
run(inRun=False)

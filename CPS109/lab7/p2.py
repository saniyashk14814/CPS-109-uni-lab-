# Write a program that generates a sequence of 20 random die tosses and that prints the die
# values, marking only the longest run, like this: 1 2 5 5 3 3 2 4 3 (2 2 2 2) 3 6 5 5 6 3 1

import random

def longest_run(values):
  longest_start = 0
  longest_length = 0
  current_start = 0
  current_length = 1

  for i in range(1, len(values)):
    if values[i] == values[i - 1]:
      current_length += 1
      if current_length > longest_length:
        longest_length = current_length
        longest_start = current_start
    else:
      current_start = i
      current_length = 1

  for i in range(len(values)):
    if longest_length > 1 and longest_start <= i < longest_start + longest_length:
      if i == longest_start:
        print("(", end=" ")
      print(values[i], end=" ")
      if i == longest_start + longest_length - 1:
        print(")", end=" ")
    else:
      print(values[i], end=" ")
  print()

values=[]
for count in range(20):
  n=random.randrange(1,7)
  values.append(n)

longest_run(values)

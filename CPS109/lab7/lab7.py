def question_1(): 
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

def question_2():
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


def question_3():
  def longestFalse(L):
    max_length = 0
    max_start = -1
    max_end = -1

    current_length = 0
    current_start = -1

    for i in range(len(L)):
      if L[i] is False:
        if current_start == -1:
          current_start = i
        current_length += 1
      else:
        if current_length > max_length:
          max_length = current_length
          max_start = current_start
          max_end = i - 1
        current_length = 0
        current_start = -1

    if current_length > max_length:
      max_length = current_length
      max_start = current_start
      max_end = len(L) - 1

    return (max_start, max_end)


  L = [False, False, True, False, False, False, False, True, True, False, False]
  print(longestFalse(L))


def question_4():
  def longestFalse(L):
    max_length = 0
    max_start = -1
    max_end = -1

    current_length = 0
    current_start = -1

    for i in range(len(L)):
      if L[i] is False:
        if current_start == -1:
          current_start = i
        current_length += 1
      else:
        if current_length > max_length:
          max_length = current_length
          max_start = current_start
          max_end = i - 1
        current_length = 0
        current_start = -1

    if current_length > max_length:
      max_length = current_length
      max_start = current_start
      max_end = len(L) - 1

    return (max_start, max_end)

  def occupy(n):
    nests = [False] * n

    for i in range(n):
      max_start, max_end = longestFalse(nests)
      middle_index = (max_start + max_end) // 2
      nests[middle_index] = True
      print(' '.join(['X' if nest else '_' for nest in nests]))

  occupy(10)

  
def question_5():
  def isPal(L):
    reversed_L = L.copy()
    reversed_L.reverse()
    if L == reversed_L:
      print("Palindrome")
    else:
      print("Not palindrome")

  L = [5, 2, 9, 9, 2, 5]
  isPal(L)




if __name__ == "__main__":
    question_1()
    question_2()
    question_3()
    question_4()
    question_5()
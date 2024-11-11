# Assume that L is a list of Boolean values, True and False. Write a function longestFalse(L)
# which returns a tuple (start, end) representing the start and end indices of the longest run
# of False values in L. If there is a tie, then return the first such run. For example, if L is:
# False False True False False False False True True False False
# 0 1 2 3 4 5 6 7 8 9 10
# Then the function would return (3, 6), since the longest run of False is from 3 to 6.


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

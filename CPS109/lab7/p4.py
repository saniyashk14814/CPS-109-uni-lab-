# Write a function occupy(n), which shows how birds are going to occupy n nests, assuming
# that each new bird will choose the nest in the middle of the largest unoccupied run of nests.
# You could use as a helper function longestFalse(L) from the previous question. For example,
# if there were 10 nests, occupy(10) would print out the following sequence, where
# underscore indicates an unoccupied nest, and X indicates an occupied nest. The first line of
# the printout is just 10 underscores showing that all the nests are unoccupied. The second
# line shows that a bird came to nest in position 5, since that is one the first middle positions
# of the unoccupied run from 0 to 9. In the third line a bird came to occupy the middle
# position for the longest open run of nests, from 0 to index 4.
# _ _ _ _ _ _ _ _ _ _
# _ _ _ _ _ X _ _ _ _
# _ _ X _ _ X _ _ _ _
# _ _ X _ _ X _ _ X _
# and so on, until
# X X X X X X X X X X

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

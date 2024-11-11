# Write a function isPal(L), where L is a list of integers, and the function returns True if the list
# is a palindrome, False otherwise. For example [5, 2, 9, 9, 2 5] is a palindrome. Use the
# reverse() method of list and check if the reversed list is the same as the original list.

def isPal(L):
  reversed_L = L.copy()
  reversed_L.reverse()
  if L == reversed_L:
    print("Palindrome")
  else:
    print("Not palindrome")

L = [5, 2, 9, 9, 2, 5]
isPal(L)

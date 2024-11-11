# Write a recursive function to add a positive integer b to another number a, add(a, b), where
# only the unit 1 can be added, For example add(5, 9) will return 14. The pseudocode is: #
# Base case: if b is 1, you can just return a + 1 # General case: otherwise, return the sum of 1
# and what is returned by adding a and b - 1.

def add(a,b):
  if b==1:
    return a+1
  else:
    return 1+add(a,b-1)
  
print(add(5,9))
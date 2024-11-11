# Here is another recursion example, but with less guidance. Write a function log2(x), which
# gives an integer approximation of the log base 2 of a positive number x, but it does so using
# recursion. Use a base case where you return 0 if x is 1 or less. In the general case, add 1 to
# the answer and divide x by 2. 

def log2(x):
  if x<=1:
    return 0
  else:
    return 1+log2(x/2)
  
print(log2(32))
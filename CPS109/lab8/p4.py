# Write a recursive function power(x, n), where n is 0 or a postive integer. For example,
# power(2, 10) will return 1024. Write a suitable base case, and for the general case use the
# idea that xn = x * xn-1 

def power(x,n):
  if n==0:
    return 1
  else:
    return x*power(x,n-1)
  
print(power(2,10))
# Improve on your function from Q4, calling it powerHalf(x, n), where this function is
# recursive like power(x, n), but it also uses the idea that xn = (xn/2)2 when n is even. Use the
# countcalls variable (as in Q5) to verify that this version of the power function is more
# efficient

def powerHalf(x,n):
  global countcalls
  countcalls=countcalls+1

  if n==0:
    return 1
  else:
    if n%2==0:
      halfPower=powerHalf(x,n//2)
      return halfPower*halfPower
    else:
      halfPower=powerHalf(x,(n-1)//2)
      return halfPower*halfPower
    
countcalls=0
print("2^10=",powerHalf(2,10))
print("Number of times the power function is called=",countcalls)
countcalls=0
print("5^10=",powerHalf(5, 10))
print("Number of times the power function is called=",countcalls)
countcalls=0
print("5^0=",powerHalf(5,0))
print("Number of times the power function is called=",countcalls)


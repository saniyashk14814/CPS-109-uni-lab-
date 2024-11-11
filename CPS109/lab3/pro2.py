n=float(input("Enter a number: "))
if n==0:
  print("Number is zero")
elif n>0:
  if abs(n)<1:
    print("Small positive")
  elif abs(n)>1000:
    print("Large positive")
  else:
    print("Positive")
else:
  if abs(n)<1:
    print("Small negative")
  elif abs(n)>1000:
    print("Large negative")
  else:
    print("Negative")

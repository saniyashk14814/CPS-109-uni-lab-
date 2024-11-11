n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))
str_len=input("Enter whether it's strict or lenient: ").strip().lower()

if str_len == "strict":
  if n1>n2>n3:
    print("Decreasing")
  elif n1<n2<n3:
    print("Increasing")
  else:
    print("Neither")
elif str_len == "lenient":
  if n1>=n2>=n3:
    print("Decreasing")
  elif n1<=n2<=n3:
    print("Increasing")
  else:
    print("Neither")
else:
  print("Invalid input please choose strict or lenient")
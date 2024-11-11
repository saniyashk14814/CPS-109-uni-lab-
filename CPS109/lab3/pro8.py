n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))
n4=int(input("Enter the fourth number: "))

if (n1==n2 and n3==n4) or (n1==n3 and n2==n4) or (n2==n3 and n1==n4):
  print("Two  pairs")
else:
  print("Not in two pair")

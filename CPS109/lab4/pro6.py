largest=0

for i in range(0,10,1):
  num=int(input("Enter a number: "))
  if num % 2 != 0:
    if num>largest:
      largest=num

if largest !=0:
  print("Largest=",largest)
else:
  print("No odd numbers")


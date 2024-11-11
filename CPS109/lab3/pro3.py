n=int(input("Enter a number: "))
n1=n
if n<0:
  n=n*(-1)

if n>1000000:
  print("Lots")
else:

 nod = 1
 while n >= 10:
   n = n// 10
   nod = nod + 1
 print("The number of digits in " , n1 , " are " , nod)



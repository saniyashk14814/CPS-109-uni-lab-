a=int(input("Enter a number: "))
sum=0
rem=0
while a>0:
  rem=int(a%10)
  if rem%2 !=0:
    sum=sum+rem
  a=a/10
print(sum)
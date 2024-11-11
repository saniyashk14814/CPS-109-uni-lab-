a=int(input("Enter a: "))
b=int(input("Enter b: "))
sum=0
for i in range(a,b+1,1):
  if i%2 !=0:
    sum=sum+i

print(sum)
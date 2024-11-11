def faro(a,b):
  r=[]
  length=int(len(a)//2)
  length1 = a[:length]
  length2 = a[length:]
  n=0
  length3=[]
  while n<length:
   
    if(b==True):
      length3.append(length1[n])
      length3.append(length2[n])
    else:
      length3.append(length2[n])
      length3.append(length1[n])
      
    n=n+1
  print(length3)

faro([1,2,3,4,5,6,7,8],False)
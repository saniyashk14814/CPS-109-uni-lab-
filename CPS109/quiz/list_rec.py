def rlen(list):
  a=list
  if(a==[]):
    return 0
  else:
    a.pop(0)
    return 1+rlen(a)
  
cnt=rlen(["a","b","c"])
print(cnt)
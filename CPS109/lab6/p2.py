# Write a function max(L) which examines the argument list L, and returns the largest object
# of type float. If there is no float object in the list, then the function returns None. For
# example:
# max([100, ‘blue’, 3.5, ‘sugar on the rocks’, 7.0]) would return 7.0, and
# max([7, 2, 9, 1]) would return None.
# Note that type(element) == float is a way to check if element is a float

def max(L):
  largest=None
  length=len(L)
  for i in range(0,length,1):
    try:
      if "." in L[i]:
        temp = float(L[i]) 
        if largest is None or temp>largest:
          largest = temp
    except:
      continue

  return largest

L=[]
n=int(input("Enter the size of the list: "))

for i in range(n):
    element = input("Enter element {}: ".format(i + 1))
    L.append(element)
result=max(L)
if result is not None:
  print("Largest float=",result)
else:
  print("No float found")

# Write a function longest(L) which examines the argument list L and returns the longest
# string. You can assume all of the elements of the list L are strings, and that the list is not
# empty. Use the approach where there is a variable largestyet which is initialized to the first
# element of L. Then go through the rest of the elements and update largestyet whenever
# you encounter a longer string. For example”
# longest(['blue', 'red', 'the white house', 'green']) would return 'the white house'.

def longest(L):
  largest = L[0]

  for s in L:
    if len(s) > len(largest):
      largest = s

  return largest

a=[]
n=int(input("Enter the size of the list: "))

for i in range(n):
    element = input("Enter element {}: ".format(i + 1))
    a.append(element)

result=longest(a)
print("Longest string=", result)
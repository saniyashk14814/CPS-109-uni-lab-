# Write a program that has a loop to read in five strings and put them into a list. Write a
# second loop to print the strings in the reverse order. This is an exercise in indexing, so do
# not use the reverse() method of list. Print the index in the following format. The actual
# strings you read in are arbitrary. Example format when running q1.py:
# Enter string 1/5: the blue moon
# Enter string 2/5: the red guitar
# Enter string 3/5: go home
# Enter string 4/5: spill the beans
# Enter string 5/5: winter in Oklahoma
# String 5/5: winter in Oklahoma
# String 4/5: spill the beans
# String 3/5: go home
# String 2/5: the red guitar
# String 1/5: the blue moon

a=[]
for i in range(0,5,1):
  element=input("Enter a string: ".format(i+1))
  a.append(element)
print("The reverse order string is:")
for i in range(4,-1,-1):
  print(a[i])
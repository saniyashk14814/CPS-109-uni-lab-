string=(input("Enter the string"))
sum=0
character=[char for char in string]
length=len(character)
for i in range(0,length,1):
  if character[i].isdigit():
    character[i]=int(character[i])
    sum=sum+character[i]

print(sum)
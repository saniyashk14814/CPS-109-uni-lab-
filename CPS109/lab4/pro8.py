string=(input("Enter the string: "))
numbers = string.split(',')
sum = 0

for number in numbers:
  sum += float(number)

print(sum)

# final_char=""
# sum=0
# for char in string:
#   final_char=""
#   if char != ",":
#     final_char=final_char+char
#   else:
#     final_char=int(final_char)
#     sum=sum+final_char

# print(sum)
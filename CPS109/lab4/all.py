def question_1(): 
  sum_even=0
  for i in range (0,101,1):
    if i % 2 ==0:
      sum_even=sum_even+i

  print(sum_even)

def question_2():
  sum_sq=0
  for i in range(1,101,1):
    sq=i*i
    sum_sq+=sq
  print(sum_sq)

def question_3():
  total=1
  for i in range(0,21,1):
    print("2^",i ,"=" , end=' ')
    total=2 ** i
    print(total)

def question_4():
  a=int(input("Enter a: "))
  b=int(input("Enter b: "))
  sum=0
  for i in range(a,b+1,1):
    if i%2 !=0:
      sum=sum+i
  print(sum)
  
def question_5():
  a=int(input("Enter a number: "))
  sum=0
  rem=0
  while a>0:
    rem=int(a%10)
    if rem%2 !=0:
      sum=sum+rem
    a=a/10
  print(sum)

def question_6():
  largest=0

  for i in range(0,10,1):
    num=int(input("Enter a number: "))
    if num % 2 != 0:
      if num>largest:
        largest=num

  if largest !=0:
    print("Largest=",largest)
  else:
    print("No odd numbers")

def question_7():
  string=(input("Enter the string: "))
  sum=0
  character=[char for char in string]
  length=len(character)
  for i in range(0,length,1):
    if character[i].isdigit():
      character[i]=int(character[i])
      sum=sum+character[i]

  print(sum)
    
def question_8():
  string=(input("Enter the string: "))
  numbers = string.split(',')
  sum = 0

  for number in numbers:
    sum += float(number)

  print(sum)

if __name__ == "__main__":
    question_1() # You can comment any of these out for testing purposes
    question_2()
    question_3()
    question_4()
    question_5()
    question_6()
    question_7()
    question_8()
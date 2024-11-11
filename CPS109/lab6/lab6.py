def question_1():
  a=[]
  for i in range(0,5,1):
    element=input("Enter a string: ".format(i+1))
    a.append(element)
  print("The reverse order string is:")
  for i in range(4,-1,-1):
    print(a[i])

def question_2():
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


def question_3():
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

def question_4():
  import random

  L = list(range(1, 101))
  T = tuple(range(1, 101))

  L_odd = []
  T_odd = ()
  for i in range(1, 101, 2):
      L_odd.append(i)
      T_odd += (i,)

  L_squares = []
  T_squares = ()
  for i in range(50):
    L_squares.append(i ** 2)
    T_squares += (i ** 2,)

  L_random = []
  T_random = ()
  for i in range(60):
    L_random.append(random.randrange(0, 50))
    T_random += (random.randrange(0, 50),)

    L_zeros = [0] * 50
  T_zeros = (0,) * 50

  print("L =", L)
  print("T =", T)
  print("L_odd =", L_odd)
  print("T_odd =", T_odd)
  print("L_squares =", L_squares)
  print("T_squares =", T_squares)
  print("L_random =", L_random)
  print("T_random =", T_random)
  print("L_zeros =", L_zeros)
  print("T_zeros =", T_zeros)

def question_5():
  L1 = [x for x in range(1, 101)]

  L2 = [x for x in range(1, 101) if x % 2 == 1]

  L3 = [x ** 2 for x in range(50)]

  import random
  L4 = [random.randrange(0, 50) for _ in range(60)]

  L5 = [0] * 50

  print("L1 =", L1)
  print("L2 =", L2)
  print("L3 =", L3)
  print("L4 =", L4)
  print("L5 =", L5)


def question_6():
  import math
  def perimeter(poly):
    x1, y1 = poly [0]
    x2, y2 = poly [1]
    distance = math.sqrt(((x2-x1) **2)+((y2-y1) **2))
    return distance
  vertices=int(input("Enter number of vertices of the polygon:"))
  coordinates = []

  for i in range(0, vertices):
    x= float(input("Enter value for x{0}: ".format(i+1)))
    y=float(input("Enter value for y{0}: ".format(i+1)))
    coordinates.append((x, y))
  peri=0
  for i in range(0, vertices):
    if (i+1)==vertices:
      peri+=perimeter( [coordinates [1], coordinates [0]])
    else:
      peri+=perimeter([coordinates[i], coordinates [i+1]])

  print(peri)

def question_7():
  import random
  def permutation(L):
    P=[]
    C=list(L)
    while C:
      i = random.randrange(0, len(C))
      P.append(C.pop(i))

    return P

  print("Permutation of range(0, 30):", permutation(range(0, 30)))

  print("Another permutation of range(0, 30):", permutation(range(0, 30)))

  print("Permutation of [19, 4, 3, 17] (1st time):", permutation([19, 4, 3, 17]))
  print("Permutation of [19, 4, 3, 17] (2nd time):", permutation([19, 4, 3, 17]))

  poly = [(0, 0), (20, 0), (20, 10), (0, 10)]
  print("Permutation of polygon (1st time):", permutation(poly))
  print("Permutation of polygon (2nd time):", permutation(poly))


if __name__ == "__main__":
    question_1() 
    question_2()
    question_3()
    question_4()
    question_5()
    question_6()
    question_7()
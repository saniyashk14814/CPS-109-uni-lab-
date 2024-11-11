# Write a function permutation(L) which returns a random permutation of L as follows:
# (0) initialize an empty list P and a copy of L: C = list(L)
# (1) Use random.randrange(0, len(C)) to get a random index, i
# (2) remove element i from the list C using pop() and
# (3) append that element to the new list P
# (4) repeat steps (1-3) until all the elements are transferred from C to P
# (5) return the new list P
# 1. Try your function on range(0, 30), which isn't a list, but it should work anyway.
# 2. Do that again to see that you get a new permutation.
# 3. Try it on [19, 4, 3, 17] two times.
# 4. Try it on poly = [(0, 0), (20, 0), (20, 10), (0, 10)] two times.
# Note: Although the random package has a function that will make a random permutation of
# a list L: random.sample(L, len(L)) in this question you shouldn't use the sample() function,
# but you should try it out once so you'll remember how to use it.
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

# 4. Write a program that makes both a list L and a tuple T with the following values:
# a) The numbers 1 to 100, inclusive.
# b) The odd numbers from 1 to 101, inclusive.
# c) The squares of numbers from 0 to 49, inclusive
# d) 60 random integers from 0 to 49, where you import random and use
# random.randrange(0, 50) to get each value.
# e) 50 zeroes, i.e., [0, 0, ...., 0] and (0, 0, ..., 0). Note, you can use repetition, as you would
# for a string.
# Do not use list comprehension for this question

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

# Print the resulting lists and tuples
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
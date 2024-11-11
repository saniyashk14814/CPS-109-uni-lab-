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
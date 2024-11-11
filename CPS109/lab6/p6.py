# Write a function perimeter(poly) which finds the perimeter of a polygon, where the input
# argument poly is a list of tuples, each tuple being the (x, y) coordinates of a point on the
# polygon. The perimeter is the sum of the distances from one point to the next, including the
# distance from the last point to the first. The distance between (x1, y1) and (x2, y2) is:
# sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2)
# Try your function on a square, a rectangle, and a triangle, where you know what the answer
# should be

import math
def perimeter(poly):
  x1, y1 =poly [0]
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
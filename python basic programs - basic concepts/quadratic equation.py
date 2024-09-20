# Program to solve quadratic equation ax^2 + bx + c = 0
import math
a = 1
b = -7
c = 12
# Discriminant
d = b**2 - 4*a*c
# Finding two solutions
sol1 = (-b + math.sqrt(d)) / (2*a)
sol2 = (-b - math.sqrt(d)) / (2*a)
print(f"Solutions: {sol1}, {sol2}")

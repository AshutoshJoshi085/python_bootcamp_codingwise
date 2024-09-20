# Program to find the area of a triangle using Heron's formula
a = 5
b = 6
c = 7
# Semi-perimeter
s = (a + b + c) / 2
# Area calculation
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(f"Area of triangle: {area}")

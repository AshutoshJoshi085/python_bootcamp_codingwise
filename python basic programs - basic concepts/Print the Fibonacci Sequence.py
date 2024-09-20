# Program to print Fibonacci sequence up to n terms
n = 10
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

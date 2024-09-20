# taking Input coordinates of the first point
x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))

# taking Input coordinates of the second point
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))

# Calculating the distance using the formula
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Output the distance
print("The distance between the two points is:", distance)

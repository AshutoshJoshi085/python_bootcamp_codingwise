# we are taking Input = principal amount
principal = float(input("Enter the principal amount: "))

# Input annual interest rate (in decimal) like if it is 10% that meain in decimal it is 
# 10/100 = 0.1
rate = float(input("Enter the annual interest rate (in decimal): "))

# Input time for which the money is invested for (in years)
time = float(input("Enter the time the money is invested for (in years): "))

# Input number of times we are calculating the interest per year
frquency = int(input("Enter the number of times the interest is compounded per year: "))

# Calculate compound interest
amount = principal * (1 + rate / frquency) ** (frquency * time)

# Output the total amount after compound interest
print("Total amount after compound interest:", amount)

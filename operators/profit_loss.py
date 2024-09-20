# taking Input the cost price and selling price from the user
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

# Calculate the difference between selling price and cost price
difference = selling_price - cost_price

# Checking using if else condition  if there's a profit or a loss
# and printing the result on screen
if difference > 0:
    print("Profit:", difference)
elif difference < 0:
    print("Loss:", -difference)
else:
    print("No profit, no loss.")

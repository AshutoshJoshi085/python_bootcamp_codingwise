number = 1634
order = len(str(number))  # Find the number of digits
sum = 0
original = number
while number > 0:
    digit = number % 10  # Get the last digit
    sum += digit ** order  # Add the digit raised to the power of the number of digits
    number = number // 10  # Remove the last digit

# Now check if the sum is equal to the original number
if sum == original:
    print('The number is an Armstrong number')
else:
    print('The number is not an Armstrong number')

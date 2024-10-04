def is_armstrong_number(num):
    # Convert the number to string to easily iterate over digits
    digits = str(num)
    num_digits = len(digits)
    
    # Calculate the sum of the digits raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == num

# Example usage
number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

# divmod


"""

The divmod() function in Python is a built-in function that takes two arguments, a dividend and a divisor, and returns a tuple containing two elements:

Quotient: The whole number result of dividing the dividend by the divisor.
Remainder: The leftover amount after the division is complete.

"""


quotient, reminder = divmod(8, 5)
print(f'Quotient : {quotient}, Reminder : {reminder}')

# Quotient : 1, Reminder : 3 - output

"""

1. Both the dividend and divisor must be numeric values.
2. If the divisor is 0, it will raise a ZeroDivisionError.
3. The quotient and remainder are always integers.
4. The function is useful for various applications, such 
    as finding the remainder of a division operation, checking for divisibility, 
    and implementing custom algorithms.

"""

# checking a number is divisible by another number

def is_divisible(num1, num2):
    result, reminder = divmod(num1, num2)
    return reminder == 0

if is_divisible(5, 3):
    print("divisible")
else:
    print("not divisible")

# not divisible - out put

if is_divisible(10, 5):
    print("divisible")
else:
    print("not divisible")

# divisible - out put
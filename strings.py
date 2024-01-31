"""
    How to reduce the line of code in if condition using the f'' string 

"""

a = 10

if a > 5:
    print("a is greater than 5")
else:
    print("a is less than 5")

#  Using the f'' string
    
print(f'{'a is greater than 5' if a > 5 else 'a is less than 5'}')


"""     Swap case  strings """

"""
It is a string’s function that converts all uppercase characters into 
lowercase and vice versa. It is used to alter the existing case of the string. 
This method creates a copy of the string which contains all the characters in the swap case

"""

string = "Hello World"

swapped_string = string.swapcase()

print(swapped_string)
# output : hELLO wORLD
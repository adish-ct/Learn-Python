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
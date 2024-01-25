"""
pass by reference

"""

"""
In Python, when you pass a mutable object (like a list or dictionary) to a function, 
changes made to the object within the function will affect the original object outside the function. 
This behavior might be considered similar to passing by reference.

However, when you pass an immutable object (like an integer or a string) to a function, changes made 
to the object within the function do not affect the original object outside the function. This behavior 
is more akin to passing by value.
"""

# Create a variable a with value 10
x = 10

# Create a variable b with value 20
y = 20

# Create a function that multiplies a and b

def multiply(a, b):
    c = a * b
    return c

# Call the multiply function and pass a and b as arguments
print(multiply(x, y))
# Result is 200 


"""
pass by value

"""

def multiply(a, b):
    c = a * b
    return c

# call the multiply function and pass values as arguments

# premitieve data

print(multiply(10, 20))



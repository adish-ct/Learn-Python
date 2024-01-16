#   MAP 

"""
map is a built-in Python function that applies a specified function to all items in an input iterable 
(e.g., a list, tuple, or string) and returns an iterator that produces the results.
"""

iterable = [1, 2, 3, 4]

def square(x):
    return x ** 2
# map expecting a function and iterable
# map(function, iterable, ...)

# function: The function to apply to each item in the iterable.
# iterable: The iterable whose elements will be processed by the function.


new_list = map(square, iterable)

# map will return an object 
print(new_list)
# <map object at 0x0000020322895BD0>

# convert into list for see the values 
print(list(new_list))
# [1, 4, 9, 16] - output


li = [10, 20, 30, 40]

# using lambda instead of function

result = map(lambda x: x * 10, li)

print(list(result))
# [100, 200, 300, 400] - Output
# zip

"""
zip is another built-in Python function that combines elements from multiple iterables (e.g., lists, tuples) into tuples. 
It returns an iterator that generates these tuples. 
"""

# syntax 

iterator1 = []
iterator2 = []
iterator3 = []

zip(iterator1, iterator2, iterator3)

name = ["apple", "banana", "orange"]
color = ["red", "yellow", "orange"]
price = [50, 45, 60]

data = zip(name, color, price)

print(data)
# it will return a zip object
# <zip object at 0x0000021111A4DAC0> - output

print(list(data))
# it will return in tuple 
# [('apple', 'red', 50), ('banana', 'yellow', 45), ('orange', 'orange', 60)] - output


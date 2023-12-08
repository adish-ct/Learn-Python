#   ENUMERATE

"""

enumerate is a built-in Python function that is used to iterate over a sequence (such as a list, tuple, or string) while 
keeping track of the index of the current item. It returns pairs of the form (index, value)

"""

# Beginner Stage 

li = ['a', 'b', 'c', 'd']

for i in range(len(li)):
    print(i, li[i])

"""
Output will be

0 a
1 b
2 c
3 d
"""


# Using enumerate

for index, value in enumerate(li):
    print(index, value)


"""
Output will be

0 a
1 b
2 c
3 d

Enumerate provided index.
"""

# we can add start value in its index also

for index, value in enumerate(li, start=1):
    print(f'index: {index}, value: {value}')


"""
Output will be like this.

index: 1, value: a
index: 2, value: b
index: 3, value: c
index: 4, value: d
"""
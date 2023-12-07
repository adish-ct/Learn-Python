# SHALLOW COPY 

"""
A shallow copy creates a new object, but does not create copies of the objects contained within the 
original object. Instead, it copies references to the objects.

Changes made to the nested objects within the copied object will affect the original object, 
and vice versa.

"""

# how to create shallow copy

import copy

original_list = [1, [2, 3], [4, 5]]
shallow_copied_list = copy.copy(original_list)

# Modifying the nested list in the shallow copy
shallow_copied_list[1][0] = 'X'

print(original_list)        # Output: [1, ['X', 3], [4, 5]]
print(shallow_copied_list)  # Output: [1, ['X', 3], [4, 5]]


# DEEP COPY

"""

A deep copy, on the other hand, creates a new object and recursively copies all objects found in 
the original object.

Changes made to the nested objects within the copied object will not affect the original object, 
and vice versa.

"""

# how to create deep copy

import copy

original_list = [1, [2, 3], [4, 5]]
deep_copied_list = copy.deepcopy(original_list)

# Modifying the nested list in the deep copy
deep_copied_list[1][0] = 'Y'

print(original_list)        # Output: [1, [2, 3], [4, 5]]
print(deep_copied_list)     # Output: [1, ['Y', 3], [4, 5]]


"""
In summary, a shallow copy creates a new object with references to the same nested objects, 
while a deep copy creates a new object with copies of all objects found in the original object.

"""
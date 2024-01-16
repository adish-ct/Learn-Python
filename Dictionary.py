""" 
A dictionary in Python is a mutable, unordered collection of key-value pairs. 
Each key must be unique within the dictionary, and it maps to a specific value. 
You can think of a dictionary as an unordered set of key-value pairs, where each key is unique.

"""

# Creating an empty dictionary
my_dict = {}

# Creating a dictionary with values
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}


# Accessing values using keys
name = my_dict['name']
age = my_dict['age']

# Using get method to avoid KeyError
city = my_dict.get('city', 'Delhi')  # If 'city' key is not present, return Delhi instead of error'


# Modifying value
my_dict['age'] = 26

# Adding a new key-value pair
my_dict['occupation'] = 'Engineer'

# Update the dictionary with key-value pairs from another dictionary.
my_dict.update({'key1': 'value1', 'key2': 'value2'})



# Removing a specific key-value pair
del my_dict['age']

# Clearing all key-value pairs
my_dict.clear()

# Deleting the entire dictionary
del my_dict

# Remove and return the value associated with the specified key.
value = my_dict.pop('key')

# Remove and return an arbitrary (key, value) pair
key, value = my_dict.popitem()



# Getting all keys and values
keys = my_dict.keys()
values = my_dict.values()

# Check if a key is in the dictionary
if 'name' in my_dict:
    print("Key 'name' exists!")

# Iterating through key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Return the number of items in the dictionary.
length = len(my_dict)

# Return a shallow copy of the dictionary.
copy_dict = my_dict.copy()



# key Features

"""
Unordered:
Dictionaries in Python are unordered collections of key-value pairs. The order of elements is not guaranteed.

Mutable:
Dictionaries are mutable, meaning you can add, modify, or remove key-value pairs after the dictionary is created.

Key Requirements:
Keys must be unique within a dictionary. If you try to add a key that already exists, it will update the existing value.

Dynamic:
Dictionaries can grow or shrink in size dynamically as key-value pairs are added or removed.

Hashable Keys:
Keys in a dictionary must be hashable. Immutable types like strings, numbers, and tuples (containing only hashable elements) 
are commonly used as keys.

Key-Value Retrieval:
Accessing a value by key in a dictionary is an O(1) operation on average, making dictionaries efficient for lookups.

Versatility:
Dictionaries can store a wide range of data types as values, including other dictionaries, lists, or even functions.

No Indexing:
Unlike lists, dictionaries do not support indexing. You access values using keys.

View Objects:
Methods like keys(), values(), and items() return view objects. These are dynamic views on the dictionary's contents 
and reflect changes.

Built-in Methods:
Dictionaries come with a variety of built-in methods for tasks like adding, updating, deleting, and querying elements.

Memory Efficiency:
While dictionaries provide fast lookups, they may use more memory compared to other data structures, especially for small datasets.


"""

# Dictionary Comprehension:
# Similar to list comprehensions, Python supports dictionary comprehensions for concise creation of dictionaries.

squares = {x: x**2 for x in range(5)}
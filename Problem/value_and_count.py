dictionary = {'a': 1, 'b': 2, 'c': 3}

keys = dictionary.keys()
values = dictionary.values()

print(keys)

print(values)


list = ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'f', 'a', 'b']

""" stored in a key-value dictionary value is its count of values"""

my_dict = {}

for i in list:
    if i not in my_dict:
        my_dict[i] = list.count(i)

print(my_dict)


""" sort with its values in a dictionary """

print(my_dict)
print(my_dict.items())

print(sorted(my_dict.items(), key=lambda x: x[1]))
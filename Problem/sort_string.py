""" Sort based on length of string """

strings = ['hello', 'hey', 'to', 'application']

# This is one way to sort
print(sorted(strings, key=len))


# This is another way to sort

i = 0
j = i

while i < len(strings):
    while j < len(strings):
        if len(strings[i]) > len(strings[j]):
            strings[i], strings[j] = strings[j], strings[i]
        j += 1
    i += 1

print(strings)


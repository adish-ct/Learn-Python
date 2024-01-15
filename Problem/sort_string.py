""" Sort based on length of string """

strings = ['hello', 'zey', 'to', 'application']

print(sorted(strings, key=len))


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


value = ['i1', 'kannur4', 'am2', 'from3']

for i in range(len(value)):
    value[i] = value[i][::-1]


print(value)

value = sorted(value)

result = ""
for i in range(len(value)):
    value[i] = value[i][1:][::-1]
    result += value[i] + " "

print(value)
print(result)


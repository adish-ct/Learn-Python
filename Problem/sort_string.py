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


value = sorted(value)

# using list comprehension
new_list = " ".join([val[1:][::-1] for val in value])
print(new_list)

result = ""
for i in range(len(value)):
    value[i] = value[i][1:][::-1]
    result += value[i] + " "

new_result = " ".join(value)

print(value)
print(result)
print(new_result)





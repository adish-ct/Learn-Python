"""
Find the second largest value in the list

"""


li = [5, 2, 10, 23, 6, 0, 7, 23, 6]

first, second = None, None

if li[0] > li[1]:
    first = li[0]
    second = li[1]

for i in li:
    if i > first:
        second = first
        first = i

print("second: ", second)

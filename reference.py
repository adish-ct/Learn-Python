""" Reference Relationship """

a = 10

b = "10"

c = 10

print("Checking a == b",a == b)
# Result is False

print("Checking a is b",a is b)
# Result is False

print("Checking a == c",a == c)
# Result is True

print("Checking a is c",a is c)
# Result is True

x = 20

y = x

z = 20

print("Checking x == y",x == y)
# Result is True

print("Checking x is y",x is y)
# Result is True




""" Rererence in the case of List """


arr1 = [1, 2, 3, 4]
arr2 = [1, 2, 3, 4]

print("Checking arr1 == arr2",arr1 == arr2)
# Result is True
print("memmory address of arr1", id(arr1))

print("Checking arr1 is arr2",arr1 is arr2)
# Result is False
print("memmory address of arr2", id(arr2))


"""     References in the case of tuple """

tuple1 = (1, 2, 3, 4)
tuple2 = (1, 2, 3, 4)

print("Checking tuple1 == tuple2",tuple1 == tuple2)
# Result is True
print("memmory address of tuple1", id(tuple1))

print("Checking tuple1 is tuple2",tuple1 is tuple2)
# Result is True

print("memmory address of tuple2", id(tuple2))



""" References in the case of dictionary """

dict1 = {1: 2, 2: 3, 3: 4}
dict2 = {1: 2, 2: 3, 3: 4}

print("Checking dict1 == dict2",dict1 == dict2)
# Result is True

print("Checking dict1 is dict2",dict1 is dict2)
# Result is False

print("memmory address of dict1", id(dict1))

print("memmory address of dict2", id(dict2))


""" References in the case of set """

set1 = {1, 2, 3, 4}
set2 = {1, 2, 3, 4}

print("Checking set1 == set2",set1 == set2)
# Result is True

print("Checking set1 is set2",set1 is set2)
# Result is False

print("memmory address of set1", id(set1))

print("memmory address of set2", id(set2))
"""  bin()   """
# converting integer into binary version 

# bin() 

x = bin(50)
print(x)
# 0b110010 - output

# slice for remove 0b
print(x[2:])
# 110010 - output

""" all ()"""

# checking all the value is true 

a = False
b = False
c = True
d = True

check_true = all([a, b, c, d])
print(check_true)
# False - output

a = True
b = True
c = True
d = True

check_true = all([a, b, c, d])
print(check_true)
# True - output

a = False
b = False
c = False
d = False

check_true = all([a, b, c, d])
print(check_true)
# False

a = 5
b = 5
c = 5
d = 5

check_true = all([a, b, c, d])
print(check_true)
# True

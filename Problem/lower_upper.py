"""
change lower to upper

"""

string = "I am adish FROM KannUr Number 2147"

for i in string:
    if i.isalpha():
        if i.islower():
            string = string.replace(i, i.upper())

print(string)